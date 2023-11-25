<template>
    <!-- visualizer
    {{ state }} -->
    <div id="cy">
    </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import cytoscape from 'cytoscape'
import  router  from '../router/index.js'

// import popper from 'cytoscape-popper'


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
        tropeData: Object
    },
    watch: {
        tropeData: function (val) {
            console.log("tropedata", this.tropeData);
            let characters = [];
            let tropes = [];
            let characterTropeList = [];
            for (const [key, val] of Object.entries(this.tropeData)) {
                tropes.push(key);
                let belongsTo = val.belongsTo;
                let tropeDescriptions = val.tropeDescription;
                for (let i = 0; i < belongsTo.length; i++) {
                    let character = belongsTo[i];
                    let tropeCharacterDescription = tropeDescriptions[i];
                    characters.push(character);
                    characterTropeList.push({
                        character: character,
                        trope: key,
                        description: tropeCharacterDescription
                    });
                }
            }

            // Make into a set
            characters = [...new Set(characters)]

            let tropeNodes = [];
            let characterNodes = [];
            let tropeEdges = [];

            for (let i = 0; i < tropes.length; i++) {
                tropeNodes.push({
                    data: {
                        id: tropes[i]
                    },
                    classes: ['trope']
                });
            }

            for (let i = 0; i < characters.length; i++) {
                characterNodes.push({
                    data: {
                        id: characters[i]
                    },
                    classes: ['character']
                });
            }

            for (let i = 0; i < characterTropeList.length; i++) {
                tropeEdges.push({
                    data: {
                        id: `${characterTropeList[i].character}-${characterTropeList[i].trope}`,
                        source: characterTropeList[i].character,
                        target: characterTropeList[i].trope,
                        label: characterTropeList[i].description
                    }
                });
            }

            let cy = cytoscape({

                container: this.cy, // container to render in
                
                elements: {// list of graph elements to start with
                    nodes: [
                        ...characterNodes,
                        ...tropeNodes
                    ],
                    edges: [
                        ...tropeEdges
                    ]
                },

                style: [ // the stylesheet for the graph
                    {
                        selector: '.character',
                        style: {
                            'background-color': 'rgba(133,76,255,1)',
                            'label': 'data(id)'
                        }
                    },
                    {
                        selector: '.trope',
                        style: {
                            'background-color': 'rgba(109,233,181,1)',
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

            cy.on('tap', 'edge', function (evt) {
                var edge = evt.target;
                let label = edge.data('label');

                // Add label to visualize
            });

            cy.on('tap', 'node', function (evt) {
                var node = evt.target;
                if (node.hasClass('character')) {
                    // Redirect to character page
                    router.push({ name: 'character page', params: { id: node.id() } });
                }
                else if (node.hasClass('trope')) {
                    // Redirect to trope page
                    router.push({ name: 'trope page', params: { id: node.id() } });
                }
            });
        }


        /*
        character: function (val) {
            this.state = 'character changed'

            let characterName = this.character.name
            let thisNode = {
                data: {
                    id: characterName,
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
            // cy.nodes()[0].popper({
            //     content: () => {
            //         var content = document.createElement('div');
            //         content.innerHTML = `<p>${cy.nodes()[0].id()}</p>`;
            //         return content;
            //     },
            //     popper: {}
            // });
            cy.on('tap', 'node', function (evt) {
                var node = evt.target;
                if (node.hasClass('character')) {
                    console.log('tapped character' + node.id());
                    // node.popper({
                    //     content: () => {
                    //         var content = document.createElement('div');
                    //         content.innerHTML = `<p>${node.id()}</p>`;
                    //         return content;
                    //     },
                    //     popper: {}
                    // })
                }
                else if (node.hasClass('trope')) {
                    console.log('tapped trope ' + node.id());
                }
            });
        }*/
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