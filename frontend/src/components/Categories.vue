<template>
  <div class="categories-page">
    <CategoryList :isDeleteMode="true" :isLimitMode="false"/>
    <CategoryForm />
  </div>
</template>

<script>
import CategoryForm from './CategoryForm.vue'
import CategoryList from './CategoryList.vue'
export default {
  name: 'Categories',
  components:{
    CategoryList,
    CategoryForm
  }
}
</script>

<style>
.categories-page{
  padding-top: 89px;
}
</style>