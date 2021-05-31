<template>
  <section class="incomes">
    <div class="container">
      <h2 class="title"><a href="">Incomes</a></h2>
      <div class="row">
        <div class="col-lg-4 col-md-6 col-xs-12">
          <div class="income">
            <h3 class="money">Money</h3>
            <p class="date">Date added: Date added</p>
          </div>
        </div>
        <div class="col-lg-4 col-md-6 col-xs-12">
          <div class="income">
            <h3 class="money">Money</h3>
            <p class="date">Date added: Date added</p>
          </div>
        </div>
        <div class="col-lg-4 col-md-6 col-xs-12">
          <div class="income">
            <h3 class="money">Money</h3>
            <p class="date">Date added: Date added</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>

export default{
  name: 'IncomeList'
}
</script>

<style>
.incomes{
  background: #eef1f2;
  padding: 60px 0;
}

.incomes .income{
  background: #fff;
  height: 120px;
  padding: 20px;
  margin-bottom: 60px;
  transition: all 0.4s ease 0s;
  border-radius: 10px;
}

.incomes .row{
  margin-bottom: -60px;
}

.incomes .income h3 p{
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
}

.incomes .income h3{
  text-align: center;
  font-size: 25px;
}

.incomes .income p{
  padding-top: 20px;
  font-size: 15px;
}

.incomes .title{
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

.incomes .title a{
  text-decoration: none;
  color: #000;
  transition: all 0.3s ease 0s;
}

.incomes .title a:hover{
  color: #47d899; 
}
</style>