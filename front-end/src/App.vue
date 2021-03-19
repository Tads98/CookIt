<template>
  <div>
    <Navbar/>
    <Index/>
    <PaginaReceita/>
    <FormReceita/>
  </div>
</template>

<script>
import Index from './components/Index.vue'
import Navbar from './components/parciais/Navbar.vue'
import PaginaReceita from './components/receitas/PaginaReceita.vue'
import FormReceita from './components/receitas/FormReceita.vue'

export default {
  name: 'App',
  components: {
    Index,
    Navbar,
    PaginaReceita,
    FormReceita,
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
