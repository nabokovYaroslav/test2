<template>
  <div class="category-form">
    <div class="container">
      <div class="form">
        <h1>Add category</h1>
        <form @submit.prevent="submit({name: name.text})">
          <div class="error" v-if="error.visible">
            <p>{{error.text}}</p>
          </div>
          <div>
            <label for="name">Name</label>
            <input :class="name.error?'error':''" type="text" id="name" @input="nameOnInput" v-model="name.text" required>
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
  name: 'CategoryForm',
  data(){
    return{
      name: {
        text: '',
        error: false,
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
      if(this.name.error){
        return true
      }
      return false
    }
  },
  methods: {
    ...mapActions('categories', {
      createCategory: 'createCategory',
    }),
    ...mapActions('user', {
      logout: 'logout'
    }),
    async submit(payload){
      try {
        this.loader = true
        if(payload.name==''){
          this.name.error = true
          throw new Error("Enter name")
        }
        await this.createCategory({name: payload.name, user: this.user.id})
        this.name.text = ''
      } catch (error) {
        if(error.response){
          const status = error.response.status
          if(status == 401){
            this.logout();
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
    nameOnInput(){
      if(this.name.error){
        this.name.error = false
      }
      this.checkError()
    },
    checkError(){
      if(!this.name.error){
        this.error.visible = false
      }
    },
  },
}
</script>

<style>
.category-form{
  padding: 60px 0;
  background: #eef1f2;
}

.category-form .form{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.category-form .form h1{
  text-transform: uppercase;
}
.category-form .form form{
  margin-top: 30px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  padding:20px;
  max-width: 90%;
  min-width: 40%;
}
.category-form .form form>div{
  display: flex;
  justify-content: center;
}
.category-form .form form>div:not(:first-child){
  margin-top: 20px;
}
.category-form .form form input, .category-form .form form select{
  margin-left: 10px;
  width: 100%;
  outline: none
}
.category-form .form form input.error, .category-form .form form select.error{
  border-color: red;
}
.category-form .form form button{
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

.category-form .form form button:hover{
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