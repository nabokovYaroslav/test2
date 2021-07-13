<template>
  <section class="incomes">
    <div class="container">
      <h2 class="title"><router-link tag="a" to="/incomes">Incomes</router-link></h2>
      <div class="row">
        <div class="col-lg-4 col-md-6 col-xs-12" v-for="i in incomesLimit" :key="i">
          <div class="income">
            <h3 class="money">{{incomes[i-1].money}}</h3>
            <p class="date">Date added: {{incomes[i-1].added_at}}</p>
            <svg class="delete-button" v-if="isDeleteMode" @click="onDeleteClick(incomes[i-1].id)">
              <use :href="deleteIcon"></use>
            </svg>
            <DeletePopup 
            :data="{id: incomes[i-1].id}" 
            v-if="deleteButtonsClicked.indexOf(incomes[i-1].id) != -1" 
            @onclick="onDeletePopupButtonClick"
            />
          </div>
        </div>
        <div class="col-xs-12" v-if="incomesIsLoading" style="display:flex; align-items: center; justify-content: center;">
          <div class="loader" style="width:100px; height:100px; border-width: 10px;"></div>
        </div>
      </div>
      <div class="showMore" v-if="!isLimitMode && !incomesIsLoading && hasNext">
        <a @click="onShowMore">Show more</a>
      </div>
    </div>
  </section>
</template>

<script>
import {mapGetters, mapActions} from 'vuex';
import icons from '@/assets/icons.svg'
import DeletePopup from './DeletePopup.vue'

export default{
  props:['isDeleteMode', 'isLimitMode'],
  name: 'IncomeList',
  data(){
    return {
      baseLimit: 6,
      deleteIcon: icons+'#delete',
      deleteButtonsClicked: [],
    }
  },
  components:{
    DeletePopup
  },
  computed:{
    ...mapGetters('incomes',{
      incomes: 'incomes',
      incomesIsLoading: 'incomesIsLoading',
      hasNext: 'hasNext'
    }),
    limit(){
      return this.incomes.length + this.baseLimit;
    },
    offset(){
      return this.limit - this.baseLimit;
    },
    incomesLimit(){
      if(this.incomes.length >= this.limit){
        return this.limit
      }
      return this.incomes.length
    }
  },
  methods:{
    ...mapActions('incomes',{
      getIncomes: 'getIncomes',
      clearIncomes: 'clearIncomes',
      deleteIncome: 'deleteIncome',
    }),
    ...mapActions('user', {
      getBalance: 'getBalance',
      logout: 'logout',
    }),
    async onShowMore(){
      try {
        await this.getIncomes({limit: this.limit, offset: this.offset})
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
          await this.deleteIncome(data.id)
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
      if(!this.incomesIsLoading){
        await this.getIncomes({limit: this.baseLimit, offset: 0})
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
    this.clearIncomes()
  }
}
</script>

<style>
.incomes{
  background: #eef1f2;
  padding: 60px 0;
}

.incomes .income{
  background: #fff;
  height: 120px;
  padding: 20px;
  margin-bottom: 60px;
  transition: all 0.4s ease 0s;
  border-radius: 10px;
  position: relative;
}

.incomes .row{
  margin-bottom: -60px;
}

.incomes .income h3 p{
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}

.incomes .income h3{
  text-align: center;
  font-size: 25px;
}

.incomes .income p{
  padding-top: 20px;
  font-size: 15px;
}

.incomes .title{
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

.incomes .title a{
  text-decoration: none;
  color: #000;
  transition: all 0.3s ease 0s;
}

.incomes .title a:hover{
  color: #47d899; 
}
.incomes .income .delete-button{
  position: absolute;
  right: 5px;
  top: 5px;
  cursor: pointer;
}
.incomes .income .delete-button{
  transition: .3s;
  width:20px;
  height:20px;
}
.incomes .income .delete-button:hover{
  fill: red
}
.incomes .showMore{
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.incomes .showMore a{
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
.incomes .showMore a:hover{
  color: #47d899;
  border-color: #47d899;
  background-color: #fff;
}
</style>