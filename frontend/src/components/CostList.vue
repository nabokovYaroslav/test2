<template>
  <section class="costs">
    <div class="container">
      <h2 class="title"><router-link tag="a" to="/costs">Costs</router-link></h2>
      <div class="row">
        <div class="col-lg-4 col-md-6 col-xs-12" v-for="i in costsLimit" :key="i">
          <div class="cost">
            <h3 class="name">{{costs[i-1].name}}</h3>
            <p class="category_name">Category name: 
              <router-link 
              tag="a" 
              :to="{name: 'category', params:{category_id: costs[i-1].category}}"
              >
                {{costs[i-1].category_name}}
              </router-link>
            </p>
            <p class="date">Date added: {{costs[i-1].added_at}}</p>
            <p class="money">Money: {{costs[i-1].money}}</p>
            <svg class="delete-button" v-if="isDeleteMode" @click="onDeleteClick(costs[i-1].id)">
              <use :href="deleteIcon"></use>
            </svg>
            <DeletePopup 
            :data="{id: costs[i-1].id}" 
            v-if="deleteButtonsClicked.indexOf(costs[i-1].id) != -1" 
            @onclick="onDeletePopupButtonClick"
            />
          </div>
        </div>
        <div class="col-xs-12" v-if="costsIsLoading" style="display:flex; align-items: center; justify-content: center;">
          <div class="loader" style="width:100px; height:100px; border-width: 10px;"></div>
        </div>
      </div>
      <div class="showMore" v-if="!isLimitMode && !costsIsLoading && hasNext">
        <a @click="onShowMore">Show more</a>
      </div>
    </div>
  </section>
</template>

<script>
import {mapGetters, mapActions} from 'vuex';
import DeletePopup from './DeletePopup.vue'
import icons from '@/assets/icons.svg'
export default{
  props:['isDeleteMode', 'isLimitMode'],
  name: 'CostList',
  data(){
    return {
      baseLimit: 6,
      deleteIcon: icons+'#delete',
      deleteButtonsClicked: []
    }
  },
  components:{
    DeletePopup
  },
  computed:{
    ...mapGetters('costs',{
      costs: 'costs',
      costsIsLoading: 'costsIsLoading',
      hasNext: 'hasNext'
    }),
    limit(){
      return this.costs.length + this.baseLimit;
    },
    offset(){
      return this.limit - this.baseLimit;
    },
    costsLimit(){
      if(this.costs.length >= this.limit){
        return this.limit
      }
      return this.costs.length
    }
  },
  methods:{
    ...mapActions('costs',{
      getCosts: 'getCosts',
      clearCosts: 'clearCosts',
      deleteCost: 'deleteCost',
    }),
    ...mapActions('user', {
      getBalance: 'getBalance',
      logout: 'logout',
    }),
    async onShowMore(){
      try {
        await this.getCosts({limit: this.limit, offset: this.offset})
      } catch (error) {
        if(error.response){
          const status = error.response.status
          if(status == 401){
            this.logout()
          }
        }
      }
    },
    onDeleteClick(id){
      this.deleteButtonsClicked.push(id)
    },
    async onDeletePopupButtonClick({action, data}){
      try {
        if(action){
          await this.deleteCost(data.id)
          await this.getBalance()
        }
        this.deleteButtonsClicked = this.deleteButtonsClicked.filter((id)=>{
          return id != data.id
        })
      } catch (error) {
        if(error.response){
          const status = error.response.status
          if(status == 401){
            this.logout()
          }
        }
      }
    }
  },
  async created(){
    try {
      if(!this.costsIsLoading){
        await this.getCosts({limit: this.baseLimit, offset: 0})
      }
    } catch (error) {
      if(error.response){
        const status = error.response.status
        if(status == 401){
          this.logout()
        }
      }
    }  
  },
  beforeDestroy(){
    this.clearCosts()
  }
}
</script>

<style>
.costs{
  background: #eef1f2;
  padding: 60px 0;
  padding-top: 149px;
}

.costs .cost{
  background: #fff;
  height: 200px;
  padding: 20px;
  margin-bottom: 60px;
  transition: all 0.4s ease 0s;
  border-radius: 10px;
}

.costs .row{
  margin-bottom: -60px;
}

.costs .cost h3 p{
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}

.costs .cost h3{
  text-align: center;
  font-size: 25px;
}

.costs .cost h3 a, .costs .cost p a{
  text-decoration: none;
  color: #000;
  transition: all 0.3s ease 0s;
  font-weight: 600;
}

.costs .cost h3 a:hover, .costs .cost p a:hover{
  color: #47d899;  
}

.costs .cost p{
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-top: 20px;
  font-size: 15px;
  
}

.costs .title{
  font-size: 45px;
  font-weight: 600;
  margin-top: 0;
  text-transform: uppercase;
  color: #333;
  line-height: 1.1;
  margin-bottom: 8px;
  text-align: center;
  margin-bottom: 20px;
}

.costs .title a{
  text-decoration: none;
  color: #000;
  transition: all 0.3s ease 0s;
}

.costs .title a:hover{
  color: #47d899; 
}
.costs .cost{
  position: relative;
}
.costs .cost .delete-button{
  position: absolute;
  right: 5px;
  top: 5px;
  cursor: pointer;
}
.costs .cost .delete-button{
  transition: .3s;
  width:20px;
  height:20px;
}
.costs .cost .delete-button:hover{
  fill: red
}
.costs .showMore{
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.costs .showMore a{
  padding: 10px 20px;
  background-color: #000;
  transition: all 0.3s;
  color: #fff;
  font-size: 12px;
  border: 3px solid #000;
  cursor: pointer;
  font-weight: 600;
  text-transform: uppercase;
}
.costs .showMore a:hover{
  color: #47d899;
  border-color: #47d899;
  background-color: #fff;
}
</style>