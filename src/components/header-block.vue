<template>
    <header id="header">
        <h1>{{headerContent.name}}</h1>
        <h2 v-html="headerContent[this.$lang]"></h2>
    </header>      
</template>

<script>
    import {header} from '../assets/content/text.json';
    
    export default {
        name: 'header-block',
        computed: {
            headerContent() {
                return header
            },
            lang() {
                return this.$lang
            }
        }
    }
</script>

<style lang="scss">
    #header {
        background: var(--boxBackgroundColour);
        
        height: 20ch;
        border-radius: 10px;
        margin: 1ch;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        grid-area: header;

        a {
            color: var(--textColour);
            text-decoration: none;
            &:hover {
                color: var(--accentColour);
            }
        }
        h1 {
            font-size:5rem;
            margin: 0px;
            color: var(--accentColour)
        }
        h2 {
            margin: 0px;
        }
    }
</style>
