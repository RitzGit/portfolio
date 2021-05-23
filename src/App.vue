<template>
    <div id="app">
        <header-block/>
        <header-navbar/>
        <content-container/>
    </div>
</template>

<script>
    import headerBlock from './components/header-block.vue'
    import contentContainer from './components/content-container.vue'
    import headerNavbar from './components/header-navbar.vue'

    export default {
        name: 'App',
        components: {
            headerBlock,
            contentContainer,
            headerNavbar
        },
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
        ". . navbar navbar navbar navbar . ."
        ". content content content content content content .";
    }
</style>
