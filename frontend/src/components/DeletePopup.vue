<template>
  <div class="delete-popup">
    <div class="loader" v-if="loader"></div>
    <template v-else>
      <h3>Are you sure?</h3>
      <div class="buttons">
        <a @click="onClick(true)">Yes</a>
        <a @click="onClick(false)">No</a>
      </div>
    </template> 
  </div>
</template>

<script>
export default {
  name: 'DeletePopup',
  props: ['data'],
  data(){
    return {
      loader: false
    }
  },
  methods:{
    onClick(action){
      if(action){
        this.loader = true
      }
      this.$emit("onclick", {
        action: action,
        data: this.data
      })
    }
  }
}
</script>

<style>
.delete-popup{
  position: absolute;
  left:0;
  top:0;
  height: 100%;
  width: 100%;
  padding: 5px;
  display:flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: rgba(0,0,0,0.7);
  z-index: 1;
  border-radius: 10px;
}
.delete-popup h3{
  text-align: center;
  color: #fff;
}
.delete-popup .buttons{
  display: flex;
  justify-content: space-around;
}
.delete-popup .buttons a{
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
.delete-popup .buttons a:hover{
  color: #47d899;
  border-color: #47d899;
  background-color: #fff;
}
</style>