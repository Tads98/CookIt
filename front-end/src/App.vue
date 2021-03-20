<template>
<<<<<<< HEAD
  <div id="app">
    <Index/>
=======
  <div>
    <Navbar/>
    <Index/>
    <PaginaReceita/>
    <FormReceita/>
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
  </div>
</template>

<script>
<<<<<<< HEAD
import HelloWorld from './components/HelloWorld.vue';
import Index from './components/Index.vue'
=======
import Index from './components/Index.vue'
import Navbar from './components/parciais/Navbar.vue'
import PaginaReceita from './components/receitas/PaginaReceita.vue'
import FormReceita from './components/receitas/FormReceita.vue'
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f

export default {
  name: 'App',
  components: {
<<<<<<< HEAD
    HelloWorld,
    Index
=======
    Index,
    Navbar,
    PaginaReceita,
    FormReceita,
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
