<template>
    <div id="app" :class="selected">
        <!--git fork corner-->
        <a href="https://github.com/RitzGit/portfolio" target="_blank">
            <svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 250 250" fill="#151513" style="position: absolute; top: 0; left: 0">
                <path fill="#fff" d="M250 0L135 115h-15l-12 27L0 250V0z"/>
                <path class="octo-arm" d="M122 109c15-9 9-19 9-19-3-7-2-11-2-11 1-7-3-2-3-2-4 5-2 11-2 11 3 10-5 15-9 16" style="-webkit-transform-origin: 120px 144px; transform-origin: 120px 144px"/>
                <path class="octo-body" d="M135 115s-4 2-5 0l-14-14c-3-2-6-3-8-3 8-11 15-24-2-41-5-5-10-7-16-7-1-2-3-7-12-11 0 0-5 3-7 16-4 2-8 5-12 9s-7 8-9 12c-14 4-17 9-17 9 4 8 9 11 11 11 0 6 2 11 7 16 16 16 30 10 41 2 0 3 1 7 5 11l12 11c1 2-1 6-1 6z"/>
            </svg>
        </a>

        <a id="theme-switch" href="#" v-on:click="toggleTheme">
            <svg v-if="selected === 'dark'" version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" xmlns:xlink="http://www.w3.org/1999/xlink" enable-background="new 0 0 512 512">
                <g>
                    <g>
                    <path d="m275.4,500.7c-135,0-244.7-109.8-244.7-244.7 1.06581e-14-134.9 109.8-244.7 244.7-244.7 8.2,0 16.4,0.4 24.6,1.2 7.2,0.7 13.5,5.2 16.5,11.7s2.4,14.2-1.6,20.2c-23,33.8-35.2,73.3-35.2,114.2 0,105 78.7,192.2 183.2,202.6 7.2,0.7 13.5,5.2 16.5,11.7 3.1,6.5 2.4,14.2-1.6,20.2-45.8,67.4-121.4,107.6-202.4,107.6zm-12.5-448c-106.5,6.5-191.2,95.2-191.2,203.3 1.42109e-14,112.3 91.4,203.7 203.7,203.7 56.4,0 109.6-23.4 147.8-63.7-46.2-11.7-88.1-36.8-120.8-72.6-41.1-45.2-63.8-103.6-63.8-164.6 0.1-37.1 8.4-73.2 24.3-106.1z"/>
                    </g>
                </g>
            </svg>
            <svg v-if="selected === 'light'" version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" xmlns:xlink="http://www.w3.org/1999/xlink" enable-background="new 0 0 512 512">
            <g>
                <g>
                <path d="m256,105.5c-83.9,0-152.2,68.3-152.2,152.2 0,83.9 68.3,152.2 152.2,152.2 83.9,0 152.2-68.3 152.2-152.2 0-84-68.3-152.2-152.2-152.2zm0,263.5c-61.4,0-111.4-50-111.4-111.4 0-61.4 50-111.4 111.4-111.4 61.4,0 111.4,50 111.4,111.4 0,61.4-50,111.4-111.4,111.4z"/>
                <path d="m256,74.8c11.3,0 20.4-9.1 20.4-20.4v-23c0-11.3-9.1-20.4-20.4-20.4-11.3,0-20.4,9.1-20.4,20.4v23c2.84217e-14,11.3 9.1,20.4 20.4,20.4z"/>
                <path d="m256,437.2c-11.3,0-20.4,9.1-20.4,20.4v22.9c0,11.3 9.1,20.4 20.4,20.4 11.3,0 20.4-9.1 20.4-20.4v-22.9c0-11.2-9.1-20.4-20.4-20.4z"/>
                <path d="m480.6,235.6h-23c-11.3,0-20.4,9.1-20.4,20.4 0,11.3 9.1,20.4 20.4,20.4h23c11.3,0 20.4-9.1 20.4-20.4 0-11.3-9.1-20.4-20.4-20.4z"/>
                <path d="m54.4,235.6h-23c-11.3,0-20.4,9.1-20.4,20.4 0,11.3 9.1,20.4 20.4,20.4h22.9c11.3,0 20.4-9.1 20.4-20.4 0.1-11.3-9.1-20.4-20.3-20.4z"/>
                <path d="M400.4,82.8L384.1,99c-8,8-8,20.9,0,28.9s20.9,8,28.9,0l16.2-16.2c8-8,8-20.9,0-28.9S408.3,74.8,400.4,82.8z"/>
                <path d="m99,384.1l-16.2,16.2c-8,8-8,20.9 0,28.9 8,8 20.9,8 28.9,0l16.2-16.2c8-8 8-20.9 0-28.9s-20.9-7.9-28.9,0z"/>
                <path d="m413,384.1c-8-8-20.9-8-28.9,0-8,8-8,20.9 0,28.9l16.2,16.2c8,8 20.9,8 28.9,0 8-8 8-20.9 0-28.9l-16.2-16.2z"/>
                <path d="m99,127.9c8,8 20.9,8 28.9,0 8-8 8-20.9 0-28.9l-16.2-16.2c-8-8-20.9-8-28.9,0-8,8-8,20.9 0,28.9l16.2,16.2z"/>
                </g>
            </g>
            </svg>
        </a>
        <header-block/>
        <header-navbar/>
        <content-container/>
    </div>
</template>

<script>
    import headerBlock from './components/header-block.vue'
    import contentContainer from './components/content-container.vue'
    import headerNavbar from './components/header-navbar.vue'
    import('./assets/styles/themes.css')

    export default {
        name: 'App',
        components: {
            headerBlock,
            contentContainer,
            headerNavbar
        },
        methods: {
            toggleTheme : function() {
                if (this.selected === "light") {
                    this.selected = "dark"
                }
                else {
                    this.selected = "light"
                }
            }
        },
        data() {
            return {
                selected: "light",
                dark: require('./assets/images/dark.svg'),
                light: require('./assets/images/light.svg')
            }
        }
    }
</script>

<style lang="scss">
    #theme-switch {
        margin:1ch;
        padding:0.5ch;
        position: absolute;
        top:0;
        right:0;

        width:3%;

        min-width: 35px;
        background: var(--boxBackgroundColour);

        border-radius: 10%;
        svg {
            fill: var(--textColour);
            &:hover {
                fill: var(--accentColour);
            }
        }
    }
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
