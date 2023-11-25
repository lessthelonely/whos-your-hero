<template>
    visualizer
    {{ state }}
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
    watch: {
        character: function (val) {
            this.state = 'character changed'

            let characterName = this.character.name
        let thisNode = {
            data: {
                    id:characterName,
                },
                classes: ['character']
            }
            // Iterate this.character.trops dictionary
            // For each trope, create a node
            // For each trope, create an edge from thisNode to the trope node
            let tropeNodes = [];
            let tropeEdges = [];
            for (const [key, value] of Object.entries(this.character.tropes)) {
                tropeNodes.push({
                    data: {
                        id: key,
                    },
                    classes: ['trope']
                })
                tropeEdges.push({
                data: {
                        id: `${this.character.name}-${key}`,
                        source: characterName,
                        target: key
                }
                })
            }

            tropeNodes = tropeNodes.splice(0, 5);
            tropeEdges = tropeEdges.splice(0, 5);

        let cy = cytoscape({

                container: this.cy, // container to render in

                elements: {// list of graph elements to start with
                    nodes: [
                thisNode,
                        ...tropeNodes
            ],
                    edges: [
                        ...tropeEdges
                    ]
                },

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
                    name: 'cose',
                    nodeRepulsion: node => {
                        if (node.hasClass('character')) {
                            console.log("Node is character")
                            return 1000000
                        }
                        console.log("Node is trope")
                        return 1000
                    }
                    // rows: 1
            }
        })

            cy.on('tap', 'node', function (evt) {
                var node = evt.target;
                if (node.hasClass('character')) {
                    console.log('tapped character' + node.id());
                }
                else if (node.hasClass('trope')) {
                    console.log('tapped trope ' + node.id());
                }
            });
        }
    },
    mounted() {
        console.log("Mounted character", this.character)
        this.cy = document.getElementById('cy')
        // if (this.character) {
        //     this.state = 'no character'
        //     return
        // }
        // this.state = 'character found'
        // console.log("My character", this.character)

        return
        // Map tropes to nodes

    }
})
</script>