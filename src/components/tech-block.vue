<template>
    <div class="tech-block">
        <h3>{{content[this.$lang].title}}</h3>
        <h4>{{content[this.$lang].lang}}</h4>
        <div class="skill_content">
            <div class="skill_brick" v-for="lang in content.skill.lang" :key="lang.name">
                <a :href="lang.link" target="_blank">
                    <img :src="lang.img" :alt="lang.name" target="_blank">
                </a>
                <div class="proficiency">
                    <span v-for="n in 5" :key="n" class="dot" v-bind:style="[(n <= lang.n) ? {'background-color' : 'var(--accentColour)'} : {'background-color' : 'var(--textColour)'}]"></span>
                </div>
            </div>
        </div>
        <h4>{{content[this.$lang].frame}}</h4>
        <div class="skill_content">
            <div class="skill_brick" v-for="frame in content.skill.frame" :key="frame.name">
                <a :href="frame.link" target="_blank">
                    <img :src="frame.img" :alt="frame.name" target="_blank">
                </a>
                <div class="proficiency">
                    <span v-for="n in 5" :key="n" class="dot" v-bind:style="[(n <= frame.n) ? {'background-color' : 'var(--accentColour)'} : {'background-color' : 'var(--textColour)'}]"></span>
                </div>
            </div>
        </div>
        <h4>{{content[this.$lang].tools}}</h4>
        <div class="skill_content">
            <div class="skill_brick" v-for="tools in content.skill.tools" :key="tools.name">
                <a :href="tools.link" target="_blank">
                    <img :src="tools.img" :alt="tools.name" target="_blank">
                </a>
                <div class="proficiency">
                    <span v-for="n in 5" :key="n" class="dot" v-bind:style="[(n <= tools.n) ? {'background-color' : 'var(--accentColour)'} : {'background-color' : 'var(--textColour)'}]"></span>
                </div>
            </div>
        </div>
    </div> 
</template>

<script>
    import {fields} from '../assets/content/text.json';

    export default {
        name: 'tech-block',
        computed: {
            content() {
                return fields['Tech']
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

        h3 {
            font-size: 2rem;
            color: var(--accentColour);
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