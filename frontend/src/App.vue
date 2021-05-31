<template>
  <div id="app">
    <Menu/>
    <router-view/>
  </div>
</template>

<script>

import Menu from "./components/Menu"

export default {
  name: 'App',
  components:{
    Menu,
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
