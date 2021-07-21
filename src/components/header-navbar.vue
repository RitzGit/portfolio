<template>
    <div id="navbar">
        <a href="#About Me">{{fields["About Me"][this.$lang].title}}</a>
        <a href="#Interests">{{fields["Interests"][this.$lang].title}}</a>
        <a href="#Projects">{{fields["Projects"][this.$lang].title}}</a>
    </div>      
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
</style>
