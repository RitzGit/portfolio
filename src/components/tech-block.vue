
<template>
    <section class="tech-block">
        <h2>{{content[language].title}}</h2>
        <div v-for="s in categories" :key="s">
            <h3>{{content[language][s]}}</h3>
            <div class="skill_content">
                <div class="skill_brick" v-for="elem in content.skill[s]" :key="elem.name">
                    <a :href="elem.link" target="_blank" rel="noopener noreferrer">
                        <img :src="elem.img" :alt="elem.name" :title="elem.name" target="_blank">
                    </a>
                    <div class="proficiency">
                        <span v-for="n in 5" :key="n" class="dot" v-bind:style="[(n <= elem.n) ? {'background-color' : 'var(--accentColour)'} : {'background-color' : 'var(--textColour)'}]"></span>
                    </div>
                </div>
            </div>
        </div>
    </section> 
</template>

<script>
    import {fields} from '../assets/content/text.json';

    export default {
        name: 'tech-block',
        computed: {
            content() {
                return fields['Tech']
            },
            categories() {
                return ['lang', 'frame', 'tools'];
            },
            language() {
                return this.$lang;
            }
        }
    }
</script>

<style lang="scss">
    .tech-block {
        background: var(--boxBackgroundColour);
        border-radius: 10px;
        margin: 1ch;
        padding: 1rem;
        font-size: 1.5rem;

        grid-column-start: 1;
        grid-column-end: 9;

        h2 {
            font-size: 2rem;
            color: var(--textColour);
        }
    }
    @media only screen and (max-width: 768px) { 
        .tech-block {
        grid-column-start: 1;
        grid-column-end: 9;
        }
        
    }
    @media only screen and (max-width: 650px) {
        .skill_content {
            flex-direction: column;
        }
    }
    .skill_content {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
    }
    .skill_brick {
        display: flex;
        height: 12rem;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        background: var(--lightHighlight);
        padding: 1rem;
        border-radius: 1rem;
        img {
            max-width: 100%;
            height: 8rem;
        }
    }
    .dot {
        height: 1.5rem;
        width: 1.5rem;
        background-color: #bbb;
        border-radius: 50%;
        display: inline-block;
        margin: 0.2rem;
    }
</style>
