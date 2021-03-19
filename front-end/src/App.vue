<template>
  <div>
    <Navbar/>
    <Index/>
  </div>
</template>

<script>
import Index from './components/Index.vue'
import Navbar from './components/Navbar.vue'


export default {
  name: 'App',
  components: {
    Index,Navbar
  }
}
</script>

<style>
</style>
