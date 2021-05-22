<template>
    <header id="header">
        <h1>Marvin Wallenfang</h1>
        <h2>{{title}}</h2>
    </header>      
</template>

<script>
export default {
  name: 'Header',
  props: {
    title: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
    #header {
        background: #1d1d1d;
        color: #e2e2e2;
        height: 20ch;
        border-radius: 5ch;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        grid-area: header;

        h1 {
            font-size:5rem;
            margin: 0px;
        }
        h2 {
            margin: 0px;
        }
    }
</style>
