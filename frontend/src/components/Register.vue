<template>
  <section class="register">
    <div class="container">
      <div class="form">
        <h1>Sign up</h1>
        <form @submit.prevent="submit">
          <div>
            <label for="username">Username</label>
            <input type="text" id="username" v-model="username" required>
          </div>
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

export default {
  name: 'register',
  data(){
    return{
      username: '',
      email: '',
      password: '',
    }
  },
  methods: {
    async submit(){
      try {
        HTTP.defaults.headers = {}
        await HTTP.post('authentication/register/', {
          user_name: this.username,
          email: this.email,
          password: this.password,
        })
        this.$router.push('/login')
      } catch (error) {
        console.log(error)
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
</style>