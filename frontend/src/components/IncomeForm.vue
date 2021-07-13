<template>
  <div class="income-form">
    <div class="container">
      <div class="form">
        <h1>Add income</h1>
        <form @submit.prevent="submit({money: money.text})">
          <div class="error" v-if="error.visible">
            <p>{{error.text}}</p>
          </div>
          <div>
            <label for="money">Money</label>
            <input :class="money.error?'error':''" type="text" id="money" @input="moneyOnInput" v-model="money.text" required>
          </div>
          <div>
            <div v-if="loader" class="loader"></div>
            <button v-else type="submit" :disabled="isButtonDisabled">Add</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'IncomeForm',
  data(){
    return{
      money: {
        text: '',
        error: false,
        pattern: /^[0-9]*[.,]?[0-9]+$/
      },
      loader: false,
      error: {
        visible: false,
        text: ''
      }
    }
  },
  computed: {
    ...mapGetters('user', {
      user: 'user'
    }),
    isButtonDisabled(){
      if(this.money.error){
        return true
      }
      return false
    }
  },
  methods: {
    ...mapActions('incomes', {
      createIncome: 'createIncome',
    }),
    ...mapActions('user', {
      getBalance: 'getBalance',
      logout: 'logout'
    }),
    async submit(payload){
      try {
        this.loader = true
        if(payload.money==''){
          this.name.error = true
          throw new Error("Enter name")
        }
         if(!this.money.pattern.test(payload.money)){
          this.money.error = true
          throw new Error("Money is in the wrong format")
        }
        await this.createIncome({money: parseFloat(payload.money.replace(/,/g, '.')).toFixed(2), user: this.user.id})
        await this.getBalance()
        this.money.text = ''
      } catch (error) {
        if(error.response){
          const status = error.response.status
          if(status == 401){
            this.logout()
          }
          if(status == 500){
            this.error.text = 'Server side error, please try again later'
          }else{
            this.error.text = 'Unknown error'
          }
        }else if(error instanceof Error){
          this.error.text = error.message
        }
        this.error.visible = true
      } finally {
        this.loader = false
      }
    },
    moneyOnInput(){
      if(this.money.error){
        this.money.error = false
      }
      this.checkError()
    },
    checkError(){
      if(!this.money.error){
        this.error.visible = false
      }
    },
  },
}
</script>

<style>
.income-form{
  padding: 60px 0;
  background: #eef1f2;
}

.income-form .form{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.income-form .form h1{
  text-transform: uppercase;
}
.income-form .form form{
  margin-top: 30px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  padding:20px;
  max-width: 90%;
  min-width: 40%;
}
.income-form .form form>div{
  display: flex;
  justify-content: center;
}
.income-form .form form>div:not(:first-child){
  margin-top: 20px;
}
.income-form .form form input, .income-form .form form select{
  margin-left: 10px;
  width: 100%;
  outline: none
}
.income-form .form form input.error, .income-form .form form select.error{
  border-color: red;
}
.income-form .form form button{
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

.income-form .form form button:hover{
  color: #47d899;
  border-color: #47d899;
  background-color: #fff;
}
.error p{
  font-style: italic;
  color: red;
  font-size: 12px;
}
</style>