<template>
    <div id="content">
        <content-block id="Über Mich" :end="5"/>
        <content-block id="Hobbies"/>
        <content-block id="Projekte"/>
    </div>  
</template>

<script>
import contentBlock from "./content-block.vue"

export default {
    components: { 
        contentBlock 
    },
    name: 'content-container'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
    #content {
        
        display: grid;
        grid-template-columns: repeat(8, 1fr);
        grid-template-rows: auto;

        padding-top: 10vh;
        grid-area: content;

        font-size: 2rem;

        p {
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
    }
</style>
