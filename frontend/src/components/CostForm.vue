<template>
  <div class="cost-form">
    <div class="container">
      <div class="form">
        <h1>Add cost</h1>
        <form @submit.prevent="submit({name: name.text, category: category.text, money: money.text})">
          <div class="error" v-if="error.visible">
            <p>{{error.text}}</p>
          </div>
          <div>
            <label for="name">Name</label>
            <input :class="name.error?'error':''" type="text" id="name" @input="nameOnInput" v-model="name.text" required>
          </div>
          <div>
            <label for="category">Category</label>
            <select :class="category.error?'error':''" id="category" @input="categoryOnInput" v-model="category.text">
              <option disabled value="">{{categoriesIsLoading?'Loading categories...':'Choose category'}}</option>
              <option v-for="(item, i) in categories" :key="i" :value="item.id">{{item.name}}</option>
            </select>
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
  name: 'CostForm',
  data(){
    return{
      name: {
        text: '',
        error: false,
      },
      category: {
        text: '',
        error: false,
      },
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
    ...mapGetters('categories', {
      categories: 'categories',
      categoriesIsLoading: 'categoriesIsLoading',
    }),
    isButtonDisabled(){
      if(this.name.error && this.category.error && this.money.error){
        return true
      }
      return false
    }
  },
  methods: {
    ...mapActions('categories', {
      getCategories: 'getCategories',
      clearCategories: 'clearCategories',
    }),
    ...mapActions('costs', {
      createCost: 'createCost'
    }),
    ...mapActions('user', {
      getBalance: 'getBalance',
      logout: 'logout'
    }),
    async submit(payload){
      try {
        this.loader = true
        if(payload.name==''){
          this.name.error = true
          throw new Error("Enter name")
        }
        if(payload.category==''){
          this.category.error = true
          throw new Error("Enter category")
        }
        if(payload.money==''){
          this.money.error = true
          throw new Error("Enter money")
        }
        if(!this.money.pattern.test(payload.money)){
          this.money.error = true
          throw new Error("Money is in the wrong format")
        }
        await this.createCost({name:payload.name, category: payload.category, money: parseFloat(payload.money.replace(/,/g, '.')).toFixed(2)})
        await this.getBalance();
        this.name.text = ''
        this.category.text = ''
        this.money.text = ''
      } catch (error) {
        if(error.response){
          const status = error.response.status
          if(status == 401){
            this.logout()
          }
          if(status == 400){
            if(error.response.data.category){
              this.category.error = true
              this.error.text = "This category doesn't exist"
            }
          }else if(status == 500){
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
    nameOnInput(){
      if(this.name.error){
        this.name.error = false
      }
      this.checkError()
    },
    categoryOnInput(){
      if(this.category.error){
        this.category.error = false
      }
      this.checkError()
    },
    moneyOnInput(){
      if(this.money.error){
        this.money.error = false
      }
      this.checkError()
    },
    checkError(){
      if(!this.name.error && !this.category.error && !this.money.error){
        this.error.visible = false
      }
    },
  },

  async created(){
    try {
      if(!this.categoriesIsLoading){
        this.getCategories({limit: null, offset: null});
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
    this.clearCategories()
  }
}
</script>

<style>
.cost-form{
  padding: 60px 0;
  background: #eef1f2;
}

.cost-form .form{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.cost-form .form h1{
  text-transform: uppercase;
}
.cost-form .form form{
  margin-top: 30px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  padding:20px;
  max-width: 90%;
  min-width: 40%;
}
.cost-form .form form>div{
  display: flex;
  justify-content: center;
}
.cost-form .form form>div:not(:first-child){
  margin-top: 20px;
}
.cost-form .form form input, .cost-form .form form select{
  margin-left: 10px;
  width: 100%;
  outline: none
}
.cost-form .form form input.error, .cost-form .form form select.error{
  border-color: red;
}
.cost-form .form form button{
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

.cost-form .form form button:hover{
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