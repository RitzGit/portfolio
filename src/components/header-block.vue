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
        
        border-radius: 10px;
        margin: 1ch;
        padding:2ch;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        text-align: center;

        grid-column-start: 2;
        grid-column-end: 8;

        a {
            color: var(--accentColour);
            text-decoration: none;
            &:hover {
                text-decoration: underline;
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
    @media only screen and (max-width: 768px) { 
        #header {
            grid-area: header;

            h1 {
            font-size:3rem;
            margin: 0px;
            color: var(--accentColour)
        }
        }
    }
</style>
