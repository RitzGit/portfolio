<template>
    <div id="content">The portfolio of Marvin Wallenfang is being built here.</div>    
</template>

<script>
export default {
  name: 'content-block'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

    @mixin flexbox() {
        display: -webkit-box;
        display: -moz-box;
        display: -ms-flexbox;
        display: -webkit-flex;
        display: flex;
    }

    #content {
        padding-top: 10vh;
        grid-area: content;

        font-size: 2rem;

        @include flexbox();
        align-items: center;
        justify-content: center;
    }
</style>
