<template>
  <div class="nav">
      <div class="container">
        <div class="menu row">
          <div class="col-xs-2 placelogo">
            <router-link
              to="/home"
            >
              <a class="logo">
                <img :src="image" alt="">
              </a>
            </router-link>
          </div>
          <div class="col-xs-10 menu-loader" v-if="userIsLoading">
            <div class="loader"></div>
          </div>
          <template v-else>
            <div class="col-xs-10 burger">
              <svg height="20px" viewBox="0 -53 384 384" width="20px" xmlns="http://www.w3.org/2000/svg"><path d="m368 154.667969h-352c-8.832031 0-16-7.167969-16-16s7.167969-16 16-16h352c8.832031 0 16 7.167969 16 16s-7.167969 16-16 16zm0 0"/><path d="m368 32h-352c-8.832031 0-16-7.167969-16-16s7.167969-16 16-16h352c8.832031 0 16 7.167969 16 16s-7.167969 16-16 16zm0 0"/><path d="m368 277.332031h-352c-8.832031 0-16-7.167969-16-16s7.167969-16 16-16h352c8.832031 0 16 7.167969 16 16s-7.167969 16-16 16zm0 0"/></svg>
            </div>
            <div class="col-lg-10 col-xs-12 links">
              <ul>
                <template v-if="authenticated">
                  <router-link 
                    v-for="(item, index) in menuList"
                    :key="index"
                    :to="item.url"
                    tag="li"
                    active-class="active"
                  >
                    <a>{{item.text}}</a>
                  </router-link>
                </template>
                
                <template v-if="!authenticated">
                  <router-link
                      to="/login"
                      tag="li"
                      active-class="active"
                  >
                    <a>Sign in</a>
                  </router-link>
                  <router-link
                      to="/register"
                      tag="li"
                      active-class="active"
                  >
                    <a>Sign up</a>
                  </router-link>
                </template>
                <template v-else>
                    <li>
                      <a href="javascript:void(0)" @click="onLogout">Logout</a>
                    </li>
                </template>
              </ul>
            </div>
          </template>
        </div>
      </div>
    </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
import image from "@/assets/logo.png";
export default {
  name: 'Menu',
  data(){
    return{
      "image": image,
    }
  },
  methods:{
    ...mapActions('user',{
      logout:'logout'
    }),
    onLogout(){
      this.logout()
    }
  },
  computed:{
    ...mapGetters('menu', {
      menuList: 'items'
    }),
    ...mapGetters('user', {
      userIsLoading: 'userIsLoading',
      authenticated: 'authenticated',
    })
  }

}
</script>

<style>
.nav .placelogo{
    display: flex;
    justify-content: flex-start;
    align-items: center;
}
.nav .burger{
    display: flex;
    justify-content: flex-end;
    align-items: center;
}

.nav .burger svg{
    fill:#fff;
    transition: all 0.2s ease 0s;
    cursor: pointer;
}

.nav .burger svg.active{
    fill: #47d899;
}

.nav .burger svg:hover{
    fill: #47d899;
}

.nav .links{
    display: flex;
    justify-content: flex-end;
    align-items: center;
    transition: all 0.8s ease-out;
}

.nav{
    position: fixed;
    padding: 8px 0;
    z-index: 2;
    width: 100%;
    transition: all 0.5s ease 0s;
    background-color:rgba(0, 0, 0, 0.5)
}

.nav.active{
    padding: 0;
    background: rgba(0,0,0,0.9);
}

.nav .menu .logo{
    padding: 4px 0 0 0;
}

.nav .menu .logo img{
    width: 50px;
}

.nav .menu ul{
    display: flex;
    align-items: center;
}

.nav .menu ul li{
    list-style-type: none;
}

.nav .menu ul li a{
    display: block;
    color: #fff;
    padding: 7px 14px;
    margin-left: 5px;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    text-decoration: none;
    transition: all 0.2s ease 0s;
}

.nav .menu ul li{
  display: block;
  color: #47d899;
  padding: 7px 14px;
  margin-left: 5px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  transition: all 0.2s ease 0s;
}

.nav .menu ul li a:hover{
    color: #47d899;
}

.nav .menu ul li a.active{
    color: #47d899;
}

@media (min-width: 1px){
    .nav .links{
        height: 0px;
        overflow: hidden;
        justify-content: flex-start;
        align-items: flex-start;
    }

    .nav .links.active{
        height: 320px;
    }

    .nav .menu ul{
        flex-direction: column;
        align-items: flex-start;
    }

    .nav .menu ul li a{
        padding: 15px 0;
    }

    .burger{
        display: block;
    }
    .burger svg{
        margin-right: 20px;
    }
}

@media (min-width: 992px){
    .nav .links{
        height: auto;
        transition: none;
        justify-content: flex-end;
        align-items: center;
    }

    .nav .menu ul li a{
        padding: 7px 14px;
    }

    .nav .menu ul{
        flex-direction: row;
        align-items: center;
    }

    .burger{
        display: none!important;
    }
}
.col-xs-10.menu-loader{
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>