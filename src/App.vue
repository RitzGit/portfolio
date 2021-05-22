<template>
    <div id="app">
        <header-block title="Undergraduate student at the University of Bonn"/>
        <content-block/>
    </div>
</template>

<script>
import headerBlock from './components/header-block.vue'
import contentBlock from './components/content-block.vue'

export default {
    name: 'App',
    components: {
        headerBlock,
        contentBlock
    }
}
</script>

<style lang="scss">
    #app {
        font-family: 'Open Sans', sans-serif;
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
