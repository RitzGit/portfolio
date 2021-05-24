<template>
    <div class="block" :id="id" :style="startEndVars">
        <h3>{{content[this.$lang].title}}</h3>
        <div v-html="content[this.$lang].contentHTML"></div>
    </div>   
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

<style scoped lang="scss">
    .block {
        background: var(--boxBackgroundColour);
        border-radius: 10px;
        margin: 1ch;
        padding: 1rem;
        font-size: 2rem;

        grid-column-start: var(--start);
        grid-column-end: var(--end);

        h3 {
            color: var(--accentColour);
        }

    }
</style>
