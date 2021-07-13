<template>
  <div id="app">
    <Menu/>
    <div class="place-for-loader" v-if="userIsLoading && !isLoginOrRegisterPage">
      <div class="loader" style="width:170px; height:170px; border-width:17px"></div>
    </div>
    <template v-else>
      <NotAuthorized v-if="!authenticated && !isLoginOrRegisterPage"/>
      <template v-else>
        <router-view/>
        <UserPanel v-if="authenticated"/>
      </template>
      
    </template>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
import Menu from "./components/Menu"
import NotAuthorized from "./components/NotAuthorized"
import UserPanel from "./components/UserPanel";

export default {
  name: 'App',
  components:{
    Menu,
    NotAuthorized,
    UserPanel,
  },
  computed:{
    ...mapGetters('user',{
      user: 'user',
      authenticated: 'authenticated',
      userIsLoading: 'userIsLoading',
    }),
    isLoginOrRegisterPage(){
      return this.$route.path == '/login' || this.$route.path == '/register'
    }
  },
  methods:{
    ...mapActions('user',{
      getUser:'getUser',
      logout: 'logout',
    })
  },
  async created(){
    try {
      await this.getUser()
    } catch (error) {
      if(error.response){
        const status = error.response.status
        if(status == 401){
          this.logout()
        }
      }
    }
  }
}
</script>

<style>
*{
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  font-family: "Montserrat",sans-serif;
}
body{
  background-color: #eef1f2;
}
.place-for-loader{
  padding-top: 60px;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
