<template>
    visualizer
    {{ state }}
    {{ character }}
    <div id="cy">
    </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import cytoscape from 'cytoscape'
import { Character } from '../stores/Character'


export default defineComponent({

    data() {
        return {
            state: String
        }
    },

    setup() {
        return {
            state: "loading"
        }
    },

    props: {
        character: Character
    },

    mounted() {
        this.cy = document.getElementById('cy')
    },

    updateGraph(newCharacter) {
        if (!this.character) {
            this.state = 'no character'
            return
        }
        this.state = 'character found'
        return
        // Map tropes to nodes
        let thisNode = {
            data: {
                id: this.character.name,
                class: 'character'
            }
        }
        let tropeNodes = this.character.tropes.map(trope => {
            return {
                data: {
                    id: trope.name,
                    class: 'trope'
                }
            }
        })

        let cy = cytoscape({

            container: myEle, // container to render in

            elements: [ // list of graph elements to start with
                thisNode,
                ...tropeNodes,
            ],

            style: [ // the stylesheet for the graph
                {
                    selector: 'node',
                    style: {
                        'background-color': '#666',
                        'label': 'data(id)'
                    }
                },

                {
                    selector: 'edge',
                    style: {
                        'width': 3,
                        'line-color': '#ccc',
                        'target-arrow-color': '#ccc',
                        'target-arrow-shape': 'triangle',
                        'curve-style': 'bezier'
                    }
                }
            ],

            layout: {
                name: 'grid',
                rows: 1
            }
        })

    },
    watch: {
        character: function (newCharacter) {
            this.updateGraph(newCharacter)
        }
    }
})
</script>