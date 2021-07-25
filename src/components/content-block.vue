<template>
    <section class="block" :id="id" :style="startEndVars">
        <h2>{{content[this.$lang].title}}</h2>
        <div v-html="content[this.$lang].contentHTML"></div>
    </section>   
</template>

<script>
    import {fields} from '../assets/content/text.json';

    export default {
        name: 'content-block',
        props: {
            id:{
                type: String,
                default: ""
            }
        },
        computed: {
            startEndVars () {
                return{
                    '--start': fields[this.id].start,
                    '--end': fields[this.id].end
                }
            },
            content() {
                return fields[this.id]
            }
        }
    }
</script>

<style lang="scss">
    
    .block {
        
        background: var(--boxBackgroundColour);
        border-radius: 10px;
        margin: 1ch;
        padding: 1rem;
        font-size: 1.5rem;

        grid-column-start: var(--start);
        grid-column-end: var(--end);
    

        h3 {
            font-size: 2rem;
            color: var(--accentColour);
        }
    }
    a {
        color: var(--accentColour);
        text-decoration: none;
        &:hover {
            text-decoration: underline;
        }
    }
    @media only screen and (max-width: 768px) { 
        .block {
        grid-column-start: 1;
        grid-column-end: 9;
        }
    }
</style>
