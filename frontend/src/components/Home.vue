<template>
  <div class="content">
    <CostList :isDeleteMode="false" :isLimitMode="true"/>
    <IncomeList :isDeleteMode="false" :isLimitMode="true"/>
    <CategoryList :isDeleteMode="false" :isLimitMode="true"/>
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
