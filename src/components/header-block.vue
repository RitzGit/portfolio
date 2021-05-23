<template>
    <header id="header">
        <h1>Marvin Wallenfang</h1>
        <h2>Bachelor Student für Informatik an der Universität Bonn</h2>
    </header>      
</template>

<script>
export default {
    name: 'header-block',
    props: {
        title:String
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
    #header {
        background: var(--boxBackgroundColour);
        
        height: 20ch;
        border-radius: 10px;
        margin: 1ch;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        grid-area: header;

        h1 {
            font-size:5rem;
            margin: 0px;
            color: var(--accentColour)
        }
        h2 {
            margin: 0px;
        }
    }
</style>
