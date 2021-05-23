<template>
    <div id="content">
        <p>Hier entsteht das Portfolio von Marvin Wallenfang</p>
        <content-block/>
        <content-block/>
        <content-block/>
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
