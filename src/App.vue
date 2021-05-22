<template>
  <div id="app">
    <Header title="Undergraduate student at the University of Bonn"/>
    <Content/>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Content from './components/Content.vue'

export default {
  name: 'App',
  components: {
    Header,
    Content
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #e2e2e2;
  display:grid;
  grid-template-columns: repeat(8, 12.5vw);
  grid-template-rows: auto;
  grid-template-areas: 
  ". header header header header header header ."
  ". navbar navbar navbar navbar navbar navbar ."
  ". content content content content content content .";
}
</style>
