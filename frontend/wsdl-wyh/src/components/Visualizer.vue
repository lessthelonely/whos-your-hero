<template>
    <div id="cy">
    </div>
    <div id="description">
        {{ selectedDescription }}
    </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import cytoscape from 'cytoscape'
import router from '../router/index.js'

// import popper from 'cytoscape-popper'

function separateWordsByCapitalLetters(inputString) {
  var wordsArray = inputString.split(/(?=[A-Z][a-z])|(?<=[a-z])(?=[A-Z0-9])/);
  
  for (var i = 0; i < wordsArray.length; i++) {
    if(wordsArray[i][wordsArray[i].length - 1] == "/" || wordsArray[i][wordsArray[i].length - 1] == "–"){
      wordsArray[i] = wordsArray[i] + wordsArray[i + 1];
      wordsArray.splice(i + 1, 1);
    }
    if(wordsArray[i].includes("&")){
      wordsArray[i] = wordsArray[i].split("&")[0] + " & " + wordsArray[i + 1];
      wordsArray.splice(i + 1, 1);
    }
    if (wordsArray[i].includes("andthe")) {
      var index = wordsArray[i].indexOf("andthe");
      var nextIndex = index + "andthe".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("andthe", " and the");
      }
    }
    if (wordsArray[i].includes("ofa")) {
      var index = wordsArray[i].indexOf("ofa");
      var nextIndex = index + "ofa".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("ofa", " of a");
      }
    }
    if (wordsArray[i].includes("ofthe")) {
      var index = wordsArray[i].indexOf("ofthe");
      var nextIndex = index + "ofthe".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("ofthe", " of the");
      }
    }
    if (wordsArray[i].includes("onthe")) {
      var index = wordsArray[i].indexOf("onthe");
      var nextIndex = index + "onthe".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("onthe", " on the");
      }
    }
    if (wordsArray[i].includes("tothe")) {
      var index = wordsArray[i].indexOf("tothe");
      var nextIndex = index + "tothe".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("tothe", " to the");
      }
    }
    if (wordsArray[i].includes("inthe")) {
      var index = wordsArray[i].indexOf("inthe");
      var nextIndex = index + "inthe".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("inthe", " in the");
      }
    }
    if (wordsArray[i].includes("the") && !(wordsArray[i].includes("of") || wordsArray[i].includes("to") || wordsArray[i].includes("on"))) {
      var index = wordsArray[i].indexOf("the");
      var nextIndex = index + "the".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("the", " the");
      }
    }
    if (wordsArray[i].includes("from")) {
      var index = wordsArray[i].indexOf("from");
      var nextIndex = index + "from".length;
      if (nextIndex == wordsArray[i].length || wordsArray[i][nextIndex] == " ") {
        wordsArray[i] = wordsArray[i].replace("from", " from");
      }
    }
    if (wordsArray[i].includes("ona")) {
      var index = wordsArray[i].indexOf("ona");
      var nextIndex = index + "ona".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("ona", " on a");
      }
    }
    if (wordsArray[i].includes("fora")) {
      var index = wordsArray[i].indexOf("fora");
      var nextIndex = index + "fora".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("fora", " for a");
      }
    }
    if (wordsArray[i].includes("witha")) {
      var index = wordsArray[i].indexOf("witha");
      var nextIndex = index + "witha".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("witha", " with a");
      }
    }
    if(wordsArray[i].includes("vs") && wordsArray[i] != "Chekhovs"){
      var index = wordsArray[i].indexOf("vs");
      var nextIndex = index + "vs".length;
      if(nextIndex == wordsArray[i].length){
        wordsArray[i] = wordsArray[i].replace("vs", " vs");
      }
    }
    if (wordsArray[i].includes("of")) {
      var index = wordsArray[i].indexOf("of");
      var nextIndex = index + "of".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("of", " of");
      }
    }
    if(wordsArray[i].includes("is") && wordsArray[i] != "Analysis" && wordsArray[i] != "Regenesis" && wordsArray[i] != "Orchis" && wordsArray[i] != "This"){
          var index = wordsArray[i].indexOf("is");
          var nextIndex = index + "is".length;
          if(nextIndex == wordsArray[i].length){
            wordsArray[i] = wordsArray[i].replace("is", " is");
          }
        }
    if(wordsArray[i].includes("or") && wordsArray[i] != "Junior" && wordsArray[i] != "Mentor" && wordsArray[i] != "Fervor" && wordsArray[i] != "Survivor" && wordsArray[i] != "Terror" && wordsArray[i] != "Liquor" && wordsArray[i] != "Minor" && wordsArray[i] != "Warrior" && wordsArray[i] != "Major" && wordsArray[i] != "Humor" && wordsArray[i] != "Motor" && !(wordsArray[i].includes("for"))){
      var index = wordsArray[i].indexOf("or");
      var nextIndex = index + "or".length;
      if(nextIndex == wordsArray[i].length){
        wordsArray[i] = wordsArray[i].replace("or", " or");
      }
    }
    if (wordsArray[i].includes("unto")) {
      var index = wordsArray[i].indexOf("unto");
      var nextIndex = index + "unto".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("unto", " unto");
      }
    }
    if (wordsArray[i].includes("to") && !(wordsArray[i].includes("unto"))) {
      var index = wordsArray[i].indexOf("to");
      var nextIndex = index + "to".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("to", " to");
      }
    }
    if(wordsArray[i].includes("a") && !(wordsArray[i].includes("on") || wordsArray[i].includes("of")) && wordsArray[i] != "Alpha" && wordsArray[i] != "Myopia" && wordsArray[i] != "Kotobukiya" && wordsArray[i] != "Necrosha" && wordsArray[i] != "Insignia" && wordsArray[i] != "Ninja" && wordsArray[i] != "Aura" && wordsArray[i] != "Extra" && wordsArray[i] != "Emma"){
          var index = wordsArray[i].indexOf("a");
          var nextIndex = index + "a".length;
          if(nextIndex == wordsArray[i].length){
            wordsArray[i] = wordsArray[i].replace("a", " a");
          }
    }
    if (wordsArray[i].includes("with")) {
      var index = wordsArray[i].indexOf("with");
      var nextIndex = index + "with".length;
      if (nextIndex == wordsArray[i].length || wordsArray[i][nextIndex] == " ") {
        wordsArray[i] = wordsArray[i].replace("with", " with");
      }
    }
    if (wordsArray[i].includes("and") && !(wordsArray[i].includes("the")) && (wordsArray[i] != "Grand") && (wordsArray[i] != "Hand")) {
      var index = wordsArray[i].indexOf("and");
      var nextIndex = index + "and".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("and", " and");
      }
    }
    if (wordsArray[i].includes("by") && !(wordsArray[i].includes("Baby"))) {
      var index = wordsArray[i].indexOf("by");
      var nextIndex = index + "by".length;
      if (nextIndex == wordsArray[i].length || wordsArray[i][nextIndex] == " ") {
        wordsArray[i] = wordsArray[i].replace("by", " by");
      }
    }
    if (wordsArray[i].includes("but")) {
      var index = wordsArray[i].indexOf("but");
      var nextIndex = index + "but".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("but", " but");
      }
    }
    if (wordsArray[i].includes("withan")) {
      var index = wordsArray[i].indexOf("withan");
      var nextIndex = index + "withan".length;
      if (nextIndex == wordsArray[i].length) {
        wordsArray[i] = wordsArray[i].replace("withan", " with an");
      }
    }
    if(wordsArray[i].includes("an") && wordsArray[i] != "Man" && wordsArray[i] != "Logan" && wordsArray[i] != "Batman" && wordsArray[i] != "Human" && wordsArray[i] != "Gunman" && wordsArray[i] != "Amazonian" && wordsArray[i] != "Spartan" && wordsArray[i] != "Deadpan" && wordsArray[i] != "Superhuman" && wordsArray[i] != "Superman" && wordsArray[i] != "Than" && wordsArray[i] != "Freudian" && wordsArray[i] != "Can" && wordsArray[i] != "Technician"){
          var index = wordsArray[i].indexOf("an");
          var nextIndex = index + "an".length;
          if(nextIndex == wordsArray[i].length){
            wordsArray[i] = wordsArray[i].replace("an", " an");
          }
    }
    if(wordsArray[i].includes("in") && wordsArray[i] != "Skin" && wordsArray[i] != "Sin" && wordsArray[i] != "Robin" && wordsArray[i] != "Cain" && wordsArray[i] != "Ronin" && wordsArray[i] != "Villain" && wordsArray[i] != "Captain" && wordsArray[i] != "Brain" && wordsArray[i] != "Again" && wordsArray[i] != "Main" && wordsArray[i] != "Chain" && wordsArray[i] != "Assassin"){
          var index = wordsArray[i].indexOf("in");
          var nextIndex = index + "in".length;
          if(nextIndex == wordsArray[i].length){
            wordsArray[i] = wordsArray[i].replace("in", " in");
          }
    }
    if (wordsArray[i].includes("as") && wordsArray[i] != "Atlas" && wordsArray[i] != "Has" && wordsArray[i] != "Was" && wordsArray[i] != "Mithras" && wordsArray[i] != "Ninjas") {
      var index = wordsArray[i].indexOf("as");
      var nextIndex = index + "as".length;
      if (nextIndex == wordsArray[i].length || wordsArray[i][nextIndex] == " ") {
        wordsArray[i] = wordsArray[i].replace("as", " as");
      }
    }
    if(wordsArray[i].includes("at") && wordsArray[i] != "Bat" && wordsArray[i] != "What" && wordsArray[i] != "Combat" && wordsArray[i] != "That" && wordsArray[i] != "Copycat" && wordsArray[i] != "Kombat" && wordsArray[i] != "Coat" && wordsArray[i] != "Cat" && wordsArray[i] != "Great"){
          var index = wordsArray[i].indexOf("at");
          var nextIndex = index + "at".length;
          if(nextIndex == wordsArray[i].length || wordsArray[i][nextIndex] == " "){
            wordsArray[i] = wordsArray[i].replace("at", " at");
          }
    }
    if (wordsArray[i].includes("for")) {
      var index = wordsArray[i].indexOf("for");
      var nextIndex = index + "for".length;
      if (nextIndex == wordsArray[i].length || wordsArray[i][nextIndex] == " ") {
        wordsArray[i] = wordsArray[i].replace("for", " for");
      }
    }
  }

  // Join the array elements with space to form the final string
  var resultString = wordsArray.join(' ');

  //remove double spaces
  resultString = resultString.replace(/\s+/g, ' ');

  return resultString;
}


export default defineComponent({

    data() {
        return {
            selectedDescription: String
        }
    },

    setup() {
        return {
            selectedDescription: null,
            selectedType: null,
            selectedName: null,
            selectedNode: null
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
                tropes.push(separateWordsByCapitalLetters(key));
                let belongsTo = val.belongsTo;
                let tropeDescriptions = val.tropeDescription;
                for (let i = 0; i < belongsTo.length; i++) {
                    let character = belongsTo[i];
                    let tropeCharacterDescription = tropeDescriptions[i];
                    characters.push(separateWordsByCapitalLetters(character));
                    characterTropeList.push({
                        character: separateWordsByCapitalLetters(character),
                        trope: separateWordsByCapitalLetters(key),
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

            let layoutBFSOptions = () => {
                return {
                    name: 'breadthfirst',
                    roots: this.selectedNode
                }
            }

            let layoutCoseOptions = {
                name: 'spread',
                nodeRepulsion: node => {
                    if (node.hasClass('character')) {
                        console.log("Node is character")
                        return 1000000
                    }
                    else if (node.hasClass('trope')) {
                        console.log("Node is trope")
                        return 1000000
                    }

                }
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
                            'background-color': 'rgba(109,233,181,1)',
                            'width': 3,
                            'line-color': '#ccc',
                            'target-arrow-color': '#ccc',
                            'target-arrow-shape': 'triangle',
                            'curve-style': 'bezier'
                        }
                    }
                ],

                layout: layoutCoseOptions
            })

            cy.on('tap', 'edge', evt => {
                var edge = evt.target;
                let label = edge.data('label');
                this.selectedDescription = label;
                this.$forceUpdate();
            });



            cy.on('tap', 'node', evt => {
                var node = evt.target;
                if (this.selectedNode != node) {
                    // Selecting one or another
                    this.selectedNode = node;
                    cy.layout(layoutBFSOptions()).run();
                }
                else {
                    // Deselecting
                    cy.layout(layoutCoseOptions).run();
                }
                if (node.hasClass('character')) {

                    // Redirect to character page
                    //separate names 
                   
                    // router.push({ name: 'character page', params: { id: node.id() } });
                }
                else if (node.hasClass('trope')) {
                    // Redirect to trope page
                    // router.push({ name: 'trope page', params: { id: node.id() } });
                }
            });
        },

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

                //layout: layoutCoseOptions
                layout: {
                    name: 'spread',
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

            cy.on('tap', 'edge', evt => {
                var edge = evt.target;
                let label = edge.data('label');
                this.selectedDescription = label;
                this.$forceUpdate();
            });



            cy.on('tap', 'node', evt => {
                var node = evt.target;
                if (this.selectedNode != node) {
                    // Selecting one or another
                    this.selectedNode = node;
                    cy.layout(layoutBFSOptions()).run();
                }
                else {
                    // Deselecting
                    cy.layout(layoutCoseOptions).run();
                }
                if (node.hasClass('character')) {

                    // Redirect to character page
                    // router.push({ name: 'character page', params: { id: node.id() } });
                }
                else if (node.hasClass('trope')) {
                    // Redirect to trope page
                    // router.push({ name: 'trope page', params: { id: node.id() } });
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