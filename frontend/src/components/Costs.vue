<template>
  <div>
    <CostList :isDeleteMode="true" :isLimitMode="false"/>
    <CostForm/>
  </div>
</template>

<script>
import CostList from './CostList.vue'
import CostForm from './CostForm.vue'
export default {
  name: 'Costs',
  components:{
    CostList,
    CostForm,
  }
}
</script>

<style>

</style>