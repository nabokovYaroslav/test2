<template>
  <section class="notAuthorized">
    <div class="container">
      <div>
        <h1>Oops... you're not authorized:(</h1>
      </div>
    </div>
  </section>
</template>

<script>

export default {
  name: 'NotAuthorized'

}
</script>

<style>
.notAuthorized{
  padding-top: 60px;
  background: #eef1f2;
  height: 100vh;
}
.notAuthorized .container{
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.notAuthorized .container>div{
  width: 50%;
  height: 30%;
  border-radius: 10px;
  background-color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
}
.notAuthorized h1{
  text-align: center;
}
</style>