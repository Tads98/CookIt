<template>
  <div>
    <Navbar/>
    <router-view/>

  </div>
</template>

<script>
import Navbar from './components/parciais/Navbar' 

export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>

<style>
  * {
    font-family: 'Montserrat', sans-serif;
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    }
  
  .descricao-tela-inicial {
      display: -webkit-box;
      -webkit-line-clamp: 4;
      /* number of lines to show */
      -webkit-box-orient: vertical;
      overflow: hidden;
      text-overflow: ellipsis;
  }

  i{
    color:black !important;
  }
</style>
