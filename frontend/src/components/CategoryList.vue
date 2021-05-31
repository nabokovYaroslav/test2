<template>
  <section class="categories">
    <div class="container">
      <h2 class="title"><a href="">Categories</a></h2>
      <div class="row">
        <div class="col-lg-4 col-md-6 col-xs-12">
          <div class="category">
            <h3 class="money"><a href="">Category name</a></h3>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>

export default{
  name: 'CategoryList'
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
</style>