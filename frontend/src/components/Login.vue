<template>
  <section class="login">
    <div class="container">
      <div class="form">
        <h1>Sign in</h1>
        <form @submit.prevent="submit">
          <div>
            <label for="email">Email</label>
            <input type="text" id="email" v-model="email" required>
          </div>
          <div>
            <label for="password">Password</label>
            <input type="password" id="password" v-model="password" required>
          </div>
          <div>
            <button type="submit">Submit</button>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>

<script>
import {HTTP} from "../api/common"

export default{

  name: 'login',
  data(){
    return{
      email: '',
      password: '',
    }
  },
  methods:{
    async submit(){
      try {
        const tokens = await HTTP.post('authentication/token/', {
          email: this.email,
          password: this.password,
        })
        localStorage.setItem('access_token', tokens.data.access)
        localStorage.setItem('refresh_token', tokens.data.refresh)
        this.$store.dispatch('user/getUser')
        this.$router.push('/home')
      } catch (error) {
        console.log(error)
      }
      
    }
  },
}
</script>

<style>
.login{
  padding-top: 60px;
  height: 100vh;
  background: #eef1f2;
}

.login .container{
  height: 100%;
}

.login .form{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: 100%;
}
.login .form h1{
  text-transform: uppercase;
}
.login .form form{
  margin-top: 30px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  padding:20px;
  max-width: 90%;
  min-width: 40%;
}
.login .form form>div{
  display: flex;
  justify-content: center;
}
.login .form form>div:not(:first-child){
  margin-top: 20px;
}
.login .form form input{
  margin-left: 10px;
  width: 100%;
  outline: none
}
.login .form form button{
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

.login .form form button:hover{
  color: #47d899;
  border-color: #47d899;
  background-color: #fff;
}
</style>