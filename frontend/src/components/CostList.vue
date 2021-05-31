<template>
  <section class="costs">
    <div class="container">
      <h2 class="title"><a href="">Costs</a></h2>
      <div class="row">
        <div class="col-lg-4 col-md-6 col-xs-12">
          <div class="cost">
            <h3 class="name"><a href="">Cost name</a></h3>
            <p class="category_name">Category name: <a href="">Category name</a></p>
            <p class="date">Date added: Date added</p>
            <p class="money">Money: Money</p>
          </div>
        </div>
        <div class="col-lg-4 col-md-6 col-xs-12">
          <div class="cost">
            <h3 class="name"><a href="">Cost name</a></h3>
            <p class="category_name">Category name: <a href="">Category name</a></p>
            <p class="date">Date added: Date added</p>
            <p class="money">Money: Money</p>
          </div>
        </div>
        <div class="col-lg-4 col-md-6 col-xs-12">
          <div class="cost">
            <h3 class="name"><a href="">Cost name</a></h3>
            <p class="category_name">Category name: <a href="">Category name</a></p>
            <p class="date">Date added: Date added</p>
            <p class="money">Money: Money</p>
          </div>
        </div>
        <div class="col-lg-4 col-md-6 col-xs-12">
          <div class="cost">
            <h3 class="name"><a href="">Cost name</a></h3>
            <p class="category_name">Category name: <a href="">Category name</a></p>
            <p class="date">Date added: Date added</p>
            <p class="money">Money: Money</p>
          </div>
        </div>
        <div class="col-lg-4 col-md-6 col-xs-12">
          <div class="cost">
            <h3 class="name"><a href="">Cost name</a></h3>
            <p class="category_name">Category name: <a href="">Category name</a></p>
            <p class="date">Date added: Date added</p>
            <p class="money">Money: Money</p>
          </div>
        </div>
        <div class="col-lg-4 col-md-6 col-xs-12">
          <div class="cost">
            <h3 class="name"><a href="">Cost name</a></h3>
            <p class="category_name">Category name: <a href="">Category name</a></p>
            <p class="date">Date added: Date added</p>
            <p class="money">Money: Money</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default{
  name: 'CostList',
}
</script>

<style>
.costs{
  background: #eef1f2;
  padding: 60px 0;
  padding-top: 149px;
}

.costs .cost{
  background: #fff;
  height: 200px;
  padding: 20px;
  margin-bottom: 60px;
  transition: all 0.4s ease 0s;
  border-radius: 10px;
}

.costs .row{
  margin-bottom: -60px;
}

.costs .cost h3 p{
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}

.costs .cost h3{
  text-align: center;
  font-size: 25px;
}

.costs .cost h3 a, .costs .cost p a{
  text-decoration: none;
  color: #000;
  transition: all 0.3s ease 0s;
  font-weight: 600;
}

.costs .cost h3 a:hover, .costs .cost p a:hover{
  color: #47d899;  
}

.costs .cost p{
  padding-top: 20px;
  font-size: 15px;
}

.costs .title{
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

.costs .title a{
  text-decoration: none;
  color: #000;
  transition: all 0.3s ease 0s;
}

.costs .title a:hover{
  color: #47d899; 
}
</style>