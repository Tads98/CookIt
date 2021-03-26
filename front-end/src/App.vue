<template>
  <div>
    <Navbar v-if="$route.name!='LoginCadastro'"/>
    <router-view />
  </div>
</template>

<script>
import Navbar from "./components/parciais/Navbar";

export default {
  name: "App",
  components: {
    Navbar,
  },
};
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

* {
  font-family: "Montserrat", sans-serif;
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}


i,
svg {
  color: black !important;
  width: 1em;
}
</style>
