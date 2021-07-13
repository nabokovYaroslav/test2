<template>
  <section class="register">
    <div class="container">
      <div class="form" v-if="!userIsLoading">
        <h1>Sign up</h1>
        <form @submit.prevent="submit({user_name: user_name.text, email: email.text, password: password.text})">
          <div class="error" v-if="error.visible">
            <p>{{error.text}}</p>
          </div>
          <div>
            <label for="username">Username</label>
            <input :class="user_name.error?'error':''" type="text" id="username" @input="usernameOnInput" v-model="user_name.text" required>
          </div>
          <div>
            <label for="email">Email</label>
            <input :class="email.error?'error':''" type="text" id="email" @input="emailOnInput" v-model="email.text" required>
          </div>
          <div>
            <label for="password">Password</label>
            <input :class="password.error?'error':''" type="password" id="password" @input="passwordOnInput" v-model="password.text" required>
          </div>
          <div>
            <div v-if="loader" class="loader"></div>
            <button v-else type="submit" :disabled="isButtonDisabled">Submit</button>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
  name: 'register',
  data(){
    return{
      user_name: {
        text: '',
        error: false,
      },
      email: {
        text: '',
        error: false,
      },
      password: {
        text: '',
        error: false,
      },
      loader: false,
      error: {
        text: '',
        visible: false,
      }
    }
  },
  computed:{
    ...mapGetters('user',{
      userIsLoading: 'userIsLoading',
      authenticated: 'authenticated'
    }),
    isButtonDisabled(){
      if(!this.user_name.error && !this.email.error && !this.password.error){
        return false
      }
      return true
    }
  },
  methods: {
    ...mapActions('user', {
      register: 'register',
      redirect: 'redirect',
    }),
    async submit(payload){
      try {
        this.loader = true
        if(payload.user_name==''){
          this.user_name.error = true
          throw new Error("Enter user_name")
        }
        if(payload.email==''){
          this.email.error = true
          throw new Error("Enter email")
        }
        if(payload.password==''){
          this.password.error = true
          throw new Error("Enter password")
        }
        await this.register(payload)
      } 
      catch (error) {
        if(error.response){
          const status = error.response.status
          if(status == 400){
            if(error.response.data.user_name && error.response.data.email){
              this.user_name.error = true
              this.email.error = true
              this.error.text = 'Users with this username and email already exist'
            }else if(error.response.data.user_name){
              this.user_name.error = true
              this.error.text = 'User with this username already exists'
            }else{
              this.email.error = true
              this.error.text = 'User with this email already exists'
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
      } 
      finally{
        this.loader = false
      }
    },
    usernameOnInput(){
      if(this.user_name.error){
        this.user_name.error = false
      }
      this.checkError()
    },
    emailOnInput(){
      if(this.email.error){
        this.email.error = false
      }
      this.checkError()
    },
    passwordOnInput(){
      if(this.password.error){
        this.password.error = false
      }
      this.checkError()
    },
    checkError(){
      if(!this.user_name.error && !this.email.error && !this.password.error){
        this.error.visible = false
      }
    }
  },
  watch:{
    userIsLoading(){
      if(this.authenticated){
        this.redirect()
      }
    }
  }
}
</script>

<style>
.register{
  padding-top: 60px;
  height: 100vh;
  background: #eef1f2;
}

.register .container{
  height: 100%;
}

.register .form{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: 100%;
}
.register .form h1{
  text-transform: uppercase;
}
.register .form form{
  margin-top: 30px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  padding:20px;
  max-width: 90%;
  min-width: 40%;
}
.register .form form>div{
  display: flex;
  justify-content: center;
}
.register .form form>div:not(:first-child){
  margin-top: 20px;
}
.register .form form input{
  margin-left: 10px;
  width: 100%;
  outline: none
}
.register .form form input.error{
  border-color: red;
}
.register .form form button{
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

.register .form form button:hover{
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