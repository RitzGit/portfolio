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
            default: 8
        },
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
    .block {
        display:grid;
        background: #1d1d1d;
        border-radius: 10px;
        margin: 1ch;
        padding: 1rem;
        font-size: 2rem;

        grid-column-start: var(--start);
        grid-column-end: var(--end);

    }
</style>
