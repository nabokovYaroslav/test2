<template>
  <section class="user-panel">
    <p class="user-name">{{user.user_name}}</p>
    <div class="loader" v-if="balanceIsLoading" style="width:19px;height:19px;border-width:1.9px"></div>
    <div class="place-balance" v-else>
      <p class="balance">Balance: {{balance}}</p>
      <a class="refresh" href="javascript:void(0)" @click="onRefreshClick">Refresh</a>
    </div>
  </section>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
export default {
  name: 'UserPanel',
  computed:{
    ...mapGetters('user', {
      user: 'user',
      balance: 'balance',
      balanceIsLoading: 'balanceIsLoading'
    }),
  },
  methods:{
    ...mapActions('user',{
      getBalance: 'getBalance',
      logout: 'logout',
    }),
    async onRefreshClick(){
      try {
        await this.getBalance()
      } catch (error) {
        if(error.response){
          const status = error.response.status
          if(status == 401){
            this.logout()
          }
        }
      }
    },
  },
  async created(){
    try {
      await this.getBalance();
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
.user-panel{
  display: flex;
  justify-content: space-between;
  padding: 10px 10px;
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #000;
}
.user-panel .place-balance{
  display: flex;
}
.user-panel .refresh {
  margin-left: 10px;
}
.user-panel .user-name{
  color: #fff
}
.user-panel .balance{
  color: #fff
}
.user-panel .refresh{
  text-decoration: none;
  color: blue;
}
</style>