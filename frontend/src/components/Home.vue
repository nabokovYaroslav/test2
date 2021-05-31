<template>
  <div class="content">
    <CostList/>
    <IncomeList/>
    <CategoryList/>
  </div>
</template>

<script>
import CostList from "./CostList"
import IncomeList from "./IncomeList"
import CategoryList from "./CategoryList"
export default{
  name: 'Home',
  components:{
    CostList,
    IncomeList,
    CategoryList
  },
}
</script>
