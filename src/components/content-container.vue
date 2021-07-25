<template>
    <main id="content">
        <content-block id="About Me"/>
        <content-block id="Interests"/>
        <content-block id="InterestsMusic"/>
        <content-block id="InterestsTeaching"/>
        <tech-block id="Tech"/>
        <content-block id="Projects"/>
        <content-block id="WebsiteProject"/>
    </main>  
</template>

<script>
    import contentBlock from "./content-block.vue"
    import TechBlock from './tech-block.vue'

    export default {
        name: 'content-container',
        components: { 
            contentBlock ,
            TechBlock
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
