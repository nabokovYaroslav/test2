<template>
  <div id="app">
    <Menu/>
    <router-view/>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import Menu from "./components/Menu"

export default {
  name: 'App',
  components:{
    Menu,
  },
  computed:{
    ...mapGetters('user',{
      user:'user'
    })
  },
  created(){
    this.$store.dispatch('user/getUser')
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
</style>
