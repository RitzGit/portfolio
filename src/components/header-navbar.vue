<template>
    <div id="navbar">
        <a href="#Über Mich">Über Mich</a>
        <a href="#Hobbies">Hobbies</a>
        <a href="#Projekte">Projekte</a>
    </div>      
</template>

<script>
export default {
    name: 'header-navbar'
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
    #navbar {
        background: var(--boxBackgroundColour);
        
        border-radius: 10px;
        padding: 1ch;

        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        align-items: center;

        grid-area: navbar;

        a {
            font-size: 1.5rem;
            text-decoration: none;
            color: var(--textColour);
            &:hover {
                color: var(--accentColour)
            }
        }
    }
</style>
