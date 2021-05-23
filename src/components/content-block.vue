<template>
    <div class="block" :id="id" :style="startEndVars">
        <h3>{{id}}</h3>
        <p>texte tesstsdhsjakdh alsjkl </p>
    </div>   
</template>

<script>
    export default {
        name: 'content-block',
        props: {
            id:{
                type: String,
                default: ""
            },
            start:{
                type: Number,
                default: 1
            },
            end:{
                type: Number,
                default: 9
            },
            contentId:{
                type: String,
                default: "default"
            },
            language:{
                type:String,
                default: "de"
            }
        },
        computed: {
            startEndVars () {
                return{
                    '--start': this.start,
                    '--end': this.end
                }
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
