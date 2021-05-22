<template>
  <div id="app">
    <Header title="Undergraduate student at the University of Bonn"/>
  </div>
</template>

<script>
import Header from './components/Header.vue'

export default {
  name: 'App',
  components: {
    Header
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  display:grid;
  grid-template-columns: repeat(8, 12.5vw);
  grid-template-rows: auto;
  grid-template-areas: 
  ". header header header header header header ."
  ". navbar navbar navbar navbar navbar navbar ."
  "content content content content content content content content";
}
</style>
