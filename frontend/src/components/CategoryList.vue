<template>
  <section class="categories">
    <div class="container">
      <h2 class="title"><router-link tag="a" to="/categories">Categories</router-link></h2>
      <div class="row">
        <div class="col-lg-4 col-md-6 col-xs-12" v-for="i in categoriesLimit" :key="i">
          <div class="category">
            <h3 class="money">{{categories[i-1].name}}</h3>
            <svg class="delete-button" v-if="isDeleteMode" @click="onDeleteClick(categories[i-1].id)">
              <use :href="deleteIcon"></use>
            </svg>
            <DeletePopup 
            :data="{id: categories[i-1].id}" 
            v-if="deleteButtonsClicked.indexOf(categories[i-1].id) != -1" 
            @onclick="onDeletePopupButtonClick"
            />
          </div>
        </div>
        <div class="col-xs-12" v-if="categoriesIsLoading" style="display:flex; align-items: center; justify-content: center;">
          <div class="loader" style="width:100px; height:100px; border-width: 10px;"></div>
        </div>
      </div>
      <div class="showMore" v-if="!isLimitMode && !categoriesIsLoading && hasNext">
        <a @click="onShowMore">Show more</a>
      </div>
    </div>
  </section>
</template>

<script>
import {mapGetters, mapActions} from 'vuex';
import icons from '@/assets/icons.svg'
import DeletePopup from './DeletePopup.vue'

export default{
  props:['isDeleteMode', 'isLimitMode'],
  name: 'CategoryList',
  data(){
    return {
      baseLimit: 6,
      deleteIcon: icons+'#delete',
      deleteButtonsClicked: [],
    }
  },
  components:{
    DeletePopup
  },
  computed:{
    ...mapGetters('categories',{
      categories: 'categories',
      categoriesIsLoading: 'categoriesIsLoading',
      hasNext: 'hasNext'
    }),
    limit(){
      return this.categories.length + this.baseLimit;
    },
    offset(){
      return this.limit - this.baseLimit;
    },
    categoriesLimit(){
      if(this.categories.length >= this.limit){
        return this.limit
      }
      return this.categories.length
    }
  },
  methods:{
    ...mapActions('categories',{
      getCategories: 'getCategories',
      clearCategories: 'clearCategories',
      deleteCategory: 'deleteCategory',
    }),
    ...mapActions('user',{
      getBalance: 'getBalance',
      logout: 'logout'
    }),
    async onShowMore(){
      try {
        await this.getCategories({limit: this.limit, offset: this.offset})
      } catch (error) {
        if(error.response){
          const status = error.response.status
          if(status == 401){
            this.logout();
          }
        }
      }
    },
    onDeleteClick(id){
      this.deleteButtonsClicked.push(id)
    },
    async onDeletePopupButtonClick({action, data}){
      try {
        if(action){
          await this.deleteCategory(data.id)
          await this.getBalance();
        }
        this.deleteButtonsClicked = this.deleteButtonsClicked.filter((id)=>{
          return id != data.id
        })
      } catch (error) {
        if(error.response){
          const status = error.response.status
          if(status == 401){
            this.logout();
          }
        }
      }
    }
  },
  async created(){
    try {
      if(!this.categoriesIsLoading){
        await this.getCategories({limit: this.baseLimit, offset: 0})
      }
    } catch (error) {
      if(error.response){
        const status = error.response.status
        if(status == 401){
          this.logout();
        }
      }
    }
  },
  beforeDestroy(){
    this.clearCategories()
  }
}
</script>

<style>
.categories{
  background: #eef1f2;
  padding: 60px 0;
}

.categories .category{
  background: #fff;
  height: 100px;
  padding: 20px;
  margin-bottom: 60px;
  transition: all 0.4s ease 0s;
  border-radius: 10px;
  position: relative;
}

.categories .row{
  margin-bottom: -60px;
}

.categories .category h3{
  text-align: center;
  font-size: 25px;
}

.categories .category h3 a{
  text-decoration: none;
  color: #000;
  transition: all 0.3s ease 0s;
  font-weight: 600;
}

.categories .category h3 a:hover{
  color: #47d899;  
}

.categories .category p{
  padding-top: 20px;
  font-size: 15px;
}

.categories .title{
  font-size: 45px;
  font-weight: 600;
  margin-top: 0;
  text-transform: uppercase;
  color: #333;
  line-height: 1.1;
  margin-bottom: 8px;
  text-align: center;
  margin-bottom: 20px;
}

.categories .title a{
  text-decoration: none;
  color: #000;
  transition: all 0.3s ease 0s;
}

.categories .title a:hover{
  color: #47d899; 
}

.categories .category .delete-button{
  position: absolute;
  right: 5px;
  top: 5px;
  cursor: pointer;
}
.categories .category .delete-button{
  transition: .3s;
  width:20px;
  height:20px;
}
.categories .category .delete-button:hover{
  fill: red
}
.categories .showMore{
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.categories .showMore a{
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
.categories .showMore a:hover{
  color: #47d899;
  border-color: #47d899;
  background-color: #fff;
}
</style>