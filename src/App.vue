<template>
    <div id="app" :class="selected">
        <header-block/>
        <header-navbar/>
        <content-container/>
    </div>
</template>

<script>
    import headerBlock from './components/header-block.vue'
    import contentContainer from './components/content-container.vue'
    import headerNavbar from './components/header-navbar.vue'
    import(`./assets/styles/themes.css`)

    export default {
        name: 'App',
        components: {
            headerBlock,
            contentContainer,
            headerNavbar
        },
        computed: {
            toggleTheme() {
                console.log(this.$theme)
                return this.$theme
            }
        },
        data() {
            return {
                selected: "light"
            }
        }
    }
</script>

<style lang="scss">
    #app {
        width: 100%;
        height: 100%;

        background: var(--backgroundColour);

        font-family: 'Open Sans', sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;

        text-align: left;
        color: var(--textColour);

        display:grid;
        grid-template-columns: repeat(8, 1fr);
        grid-template-rows: auto;
        grid-template-areas: 
        ". header header header header header header ."
        ". . navbar navbar navbar navbar . ."
        "content content content content content content content content";
    }
</style>
