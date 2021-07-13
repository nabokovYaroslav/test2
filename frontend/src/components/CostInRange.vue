<template>
  <section class="cost-in-range">
    <div class="container">
      <div class="form">
        <h1>Cost in range</h1>
        <form @submit.prevent="submit({startDate: startDate.text, endDate: endDate.text, categories: selectedCategories.items})">
          <div class="error" v-if="error.visible">
            <p>{{error.text}}</p>
          </div>
          <div>
            <label for="startDate">From date</label>
            <input :class="startDate.error?'error':''" type="date" id="startDate" @input="startDateOnInput" v-model="startDate.text" required>
          </div>
          <div>
            <label for="endDate">To date</label>
            <input :class="endDate.error?'error':''" type="date" id="endDate" @input="endDateOnInput" v-model="endDate.text" required>
          </div>
          <div>
            <label for="category">Categories</label>
            <select id="category" v-model="selectedCategories.items" multiple @input="categoryOnInput">
              <option disabled value="">{{categoriesIsLoading?'Loading categories...':'Choose categories'}}</option>
              <option v-for="(item, i) in categories" :key="i" :value="item.id">{{item.name}}</option>
            </select>
          </div>
          <div>
            <div v-if="loader" class="loader"></div>
            <button v-else type="submit" :disabled="isButtonDisabled">Submit</button>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'CostInRange',
  data(){
    return {
      startDate:{
        text: '',
        error: false,
      },
      endDate:{
        text: '',
        error: false,
      },
      selectedCategories: {
        items: [],
        error: false,
      },
      loader: false,
      error:{
        text: '',
        visible: false,
      },
    }
  },
  computed:{
    ...mapGetters('categories',{
      categories: 'categories',
      categoriesIsLoading: 'categoriesIsLoading'
    }),
    isButtonDisabled(){
      if(this.startDate.error || this.endDate.error || this.selectedCategories.error){
        return true
      }
      return false
    }
  },
  methods:{
    ...mapActions('categories',{
      getCategories: 'getCategories',
      clearCategories: 'clearCategories',
      getCostInRange: 'getCostInRange',
    }),
    ...mapActions('user', {
      logout: 'logout',
    }),
    startDateOnInput(){
      if(this.startDate.error){
        this.startDate.error = false
      }
      this.checkError()
    },
    endDateOnInput(){
      if(this.endDate.error){
        this.endDate.error = false
      }
      this.checkError()
    },
    categoryOnInput(){
      if(this.selectedCategories.error){
        this.selectedCategories.error = false
      }
      this.checkError()
    },
    checkError(){
      if(!this.startDate.error && !this.endDate.error && !this.selectedCategories.error){
        this.error.visible = false
      }
    },
    async submit(payload){
      try {
        this.loader = true
        const cost = await this.getCostInRange(payload)
        alert(cost.cost)
      } catch (error) {
        if(error.response){
          const status = error.response.status
          if(status == 401){
            this.logout()
          }
          if(status == 400){
            this.error.text = error.response.data.description
          }else{
            this.error.text = 'Unknown Error'
          }
        }
        this.error.visible = true
      } finally {
        this.loader = false
      }
    }
  },
  async created(){
    try {
      await this.getCategories({limit: null, offset: null})
    } catch (error) {
      if(error.response){
        const status = error.response.status
        if(status == 401){
          this.logout()
        }
      }
    }
  },
  beforeDestroy(){
    this.clearCategories();
  }
}
</script>

<style>
.cost-in-range{
  padding-top: 149px;
  height: 100vh;
  background: #eef1f2;
}

.cost-in-range .container{
  height: 100%;
}

.cost-in-range .form{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: 100%;
}
.cost-in-range .form h1{
  text-transform: uppercase;
}
.cost-in-range .form form{
  margin-top: 30px;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  padding:20px;
  max-width: 90%;
  min-width: 40%;
}
.cost-in-range .form form>div{
  display: flex;
  justify-content: center;
  align-items: center;
}
.cost-in-range .form form>div:not(:first-child){
  margin-top: 20px;
}
.cost-in-range .form form input, .cost-in-range .form form select{
  margin-left: 10px;
  width: 100%;
  outline: none
}
.cost-in-range .form form input.error{
  border-color: red;
}
.cost-in-range .form form button{
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

.cost-in-range .form form button:hover{
  color: #47d899;
  border-color: #47d899;
  background-color: #fff;
}
.error p{
  font-style: italic;
  color: red;
  font-size: 12px;
}
</style>