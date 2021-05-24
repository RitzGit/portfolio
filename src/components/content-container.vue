<template>
    <div id="content">
        <content-block id="About Me"/>
        <content-block id="Hobbies"/>
        <content-block id="Projects"/>
    </div>  
</template>

<script>
    import contentBlock from "./content-block.vue"

    export default {
        name: 'content-container',
        components: { 
            contentBlock 
        }
    }
</script>

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
