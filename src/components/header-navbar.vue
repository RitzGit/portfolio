<template>
    <nav id="navbar">
        <a href="#About Me">{{fields["About Me"][this.$lang].title}}</a>
        <a href="#Interests">{{fields["Interests"][this.$lang].title}}</a>
        <a href="#Tech">{{fields["Tech"][this.$lang].title}}</a>
        <a href="#Projects">{{fields["Projects"][this.$lang].title}}</a>
    </nav>      
</template>

<script>
    import {fields} from '../assets/content/text.json';

    export default {
        name: 'header-navbar',
        computed: {
            fields() {
                return fields;
            }
        }
    }
</script>

<style scoped lang="scss">
    #navbar {
        background: var(--boxBackgroundColour);
        
        border-radius: 10px;
        padding: 1ch;

        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        align-items: center;

        grid-area: navbar;

        a {
            font-size: 1.5rem;
            text-decoration: none;
            color: var(--accentColour);
            &:hover {
                text-decoration: underline;
            }
        }
    }
    @media only screen and (max-width: 1000px) { 
        #navbar {
            flex-direction: column;
            grid-column-start: 3;
            grid-column-end: 7;
            a {
                padding-top: 1rem;
                padding-bottom: 1rem;
            }
        }
    }
    @media only screen and (min-width: 750px) and (max-width: 1000px) { 
        #navbar {
            flex-direction: column;
            grid-column-start: 4;
            grid-column-end: 6;
            a {
                padding-top: 1rem;
                padding-bottom: 1rem;
            }
        }
    }
</style>
