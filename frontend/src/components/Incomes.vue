<template>
  <div class="incomes-page">
    <IncomeList :isDeleteMode="true" :isLimitMode="false"/>
    <IncomeForm />
  </div>
</template>

<script>
import IncomeList from './IncomeList.vue'
import IncomeForm from './IncomeForm.vue'
export default {
  name: 'Incomes',
  components:{
    IncomeList,
    IncomeForm
  }
}
</script>

<style>
.incomes-page{
  padding-top: 89px;
}
</style>