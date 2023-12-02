<template>
    <div class="row" style="display: flex; flex-direction: row; width: 100%; padding: 0px;">
        <div id="cy">
        </div>
        <div class="row" style="margin-top: 15px; justify-content: center;">
            <div style="width: 10%;">
                <input type="checkbox" class="form-check-input" id="trope-checkbox" name="trope" value="trope" checked>
                <label for="trope">Trope</label>
            </div>
            <div style="width: 10%;">

                <input type="checkbox" class="form-check-input" id="power-checkbox" name="power" value="power" checked>
                <label for="power">Power</label>
            </div>
            <div style="width: 10%;">
                <input type="checkbox" class="form-check-input" id="storyArc-checkbox" name="storyArc" value="storyArc" checked>
                <label for="storyArc">Story Arc</label>
            </div>
            <div style="width: 10%;">
                <input type="checkbox" class="form-check-input" id="media-checkbox" name="media" value="media" checked>
                <label for="media">Media</label>
            </div>
            <div style="width: 20%;">
                <input type="checkbox" class="form-check-input" id="variant-checkbox" name="variant" value="variant" checked>
                <label for="variant">Alternate Versions</label>
            </div>
        </div>
    </div>

    <div id="description" style="margin-top: 25px;" v-if="this.selectedDescription != null">
        <CharacterTrope :name="selectedDescriptionCharacter" :description="selectedDescription"
            :iteration="selectedDescriptionCharacter + ' iteration of ' + selectedDescriptionTrope" />
    </div>
    <div class="row" v-if="this.showButton()">
        <div id="router-button" class="btn btn-primary" style="width: 100;" @click="goToPage()">
            Go to Page
        </div>
    </div>
</template>

<script>
import { defineComponent, ref, onMounted } from 'vue'
import cytoscape from 'cytoscape'
import router from '../router/index.js'
import CharacterTrope from './CharacterTrope.vue'

// import popper from 'cytoscape-popper'

function separateWordsByCapitalLetters(inputString) {
    var wordsArray = inputString.split(/(?=[A-Z][a-z])|(?<=[a-z])(?=[A-Z0-9])/);

    for (var i = 0; i < wordsArray.length; i++) {
        if (wordsArray[i][wordsArray[i].length - 1] == "/" || wordsArray[i][wordsArray[i].length - 1] == "–") {
            wordsArray[i] = wordsArray[i] + wordsArray[i + 1];
            wordsArray.splice(i + 1, 1);
        }
        if (wordsArray[i].includes("&")) {
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
        if (wordsArray[i].includes("vs") && wordsArray[i] != "Chekhovs") {
            var index = wordsArray[i].indexOf("vs");
            var nextIndex = index + "vs".length;
            if (nextIndex == wordsArray[i].length) {
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
        if (wordsArray[i].includes("is") && wordsArray[i] != "Analysis" && wordsArray[i] != "Regenesis" && wordsArray[i] != "Orchis" && wordsArray[i] != "This") {
            var index = wordsArray[i].indexOf("is");
            var nextIndex = index + "is".length;
            if (nextIndex == wordsArray[i].length) {
                wordsArray[i] = wordsArray[i].replace("is", " is");
            }
        }
        if (wordsArray[i].includes("or") && wordsArray[i] != "Junior" && wordsArray[i] != "Mentor" && wordsArray[i] != "Fervor" && wordsArray[i] != "Survivor" && wordsArray[i] != "Terror" && wordsArray[i] != "Liquor" && wordsArray[i] != "Minor" && wordsArray[i] != "Warrior" && wordsArray[i] != "Major" && wordsArray[i] != "Humor" && wordsArray[i] != "Motor" && wordsArray[i] != "Determinator" && !(wordsArray[i].includes("for"))) {
            var index = wordsArray[i].indexOf("or");
            var nextIndex = index + "or".length;
            if (nextIndex == wordsArray[i].length) {
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
        if (wordsArray[i].includes("a") && !(wordsArray[i].includes("on") || wordsArray[i].includes("of")) && wordsArray[i] != "Alpha" && wordsArray[i] != "Myopia" && wordsArray[i] != "Kotobukiya" && wordsArray[i] != "Necrosha" && wordsArray[i] != "Insignia" && wordsArray[i] != "Ninja" && wordsArray[i] != "Aura" && wordsArray[i] != "Extra" && wordsArray[i] != "Emma") {
            var index = wordsArray[i].indexOf("a");
            var nextIndex = index + "a".length;
            if (nextIndex == wordsArray[i].length) {
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
        if (wordsArray[i].includes("an") && wordsArray[i] != "Man" && wordsArray[i] != "Logan" && wordsArray[i] != "Batman" && wordsArray[i] != "Human" && wordsArray[i] != "Gunman" && wordsArray[i] != "Amazonian" && wordsArray[i] != "Spartan" && wordsArray[i] != "Deadpan" && wordsArray[i] != "Superhuman" && wordsArray[i] != "Superman" && wordsArray[i] != "Than" && wordsArray[i] != "Freudian" && wordsArray[i] != "Can" && wordsArray[i] != "Technician") {
            var index = wordsArray[i].indexOf("an");
            var nextIndex = index + "an".length;
            if (nextIndex == wordsArray[i].length) {
                wordsArray[i] = wordsArray[i].replace("an", " an");
            }
        }
        if (wordsArray[i].includes("in") && wordsArray[i] != "Skin" && wordsArray[i] != "Sin" && wordsArray[i] != "Robin" && wordsArray[i] != "Cain" && wordsArray[i] != "Ronin" && wordsArray[i] != "Villain" && wordsArray[i] != "Captain" && wordsArray[i] != "Brain" && wordsArray[i] != "Again" && wordsArray[i] != "Main" && wordsArray[i] != "Chain" && wordsArray[i] != "Assassin") {
            var index = wordsArray[i].indexOf("in");
            var nextIndex = index + "in".length;
            if (nextIndex == wordsArray[i].length) {
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
        if (wordsArray[i].includes("at") && wordsArray[i] != "Bat" && wordsArray[i] != "What" && wordsArray[i] != "Combat" && wordsArray[i] != "That" && wordsArray[i] != "Copycat" && wordsArray[i] != "Kombat" && wordsArray[i] != "Coat" && wordsArray[i] != "Cat" && wordsArray[i] != "Great") {
            var index = wordsArray[i].indexOf("at");
            var nextIndex = index + "at".length;
            if (nextIndex == wordsArray[i].length || wordsArray[i][nextIndex] == " ") {
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

    components: {
        CharacterTrope
    },

    data() {
        return {
            selectedDescription: String
        }
    },

    setup() {
        return {
            cyElem: null,
            cy: null,
            selectedDescription: null,
            selectedType: null,
            selectedName: null,
            selectedNode: null
        }
    },

    props: {
        graphData: Object,
    },
    methods: {
        goToPage() {
            if (this.selectedNode == null) {
                return
            }
            let id = this.selectedNode.data('id')

            //console.log(pageId);

            if (this.selectedNode.hasClass('character')) {
                let pageId = id.split(" ").join("_").toLowerCase()

                // Redirect to character page
                router.push({ name: 'character page', params: { id: pageId } });
            }
            else if (this.selectedNode.hasClass('trope')) {
                let pageId = id.split(" ").join("")
                // Redirect to trope page
                router.push({ name: 'trope page', params: { id: pageId } });
            }

        },

        showButton() {
            if (this.selectedNode == null) {
                return false;
            }

            if (this.selectedNode.hasClass('character')) {
                return true;
            }
            else if (this.selectedNode.hasClass('trope')) {
                return true;
            }
            else if (this.selectedNode.hasClass('power')) {
                return false;
            }
            else if (this.selectedNode.hasClass('storyArc')) {
                return false;
            }
            else if (this.selectedNode.hasClass('media')) {
                return false;
            }
            else if (this.selectedNode.hasClass('variant')) {
                return false;
            }
            else {
                return false;
            }
        },
        updateVisibleNodes(e) {
            if (this.cy == null) {
                return
            }
            let target = e.target.value

            this.cy.style().selector('.' + target).style({
                'display': e.target.checked ? 'element' : 'none'
            }).update()
        }
    },

    watch: {
        graphData: function (val) {
            this.tropeData = this.graphData.tropeData;
            this.powerData = this.graphData.powerData;
            this.storyArcData = this.graphData.storyArcData;
            this.mediaData = this.graphData.mediaData;
            this.variantData = this.graphData.variantData;

            console.log("tropedata", this.tropeData);
            let characters = [];
            let tropes = [];
            let powers = [];
            let storyArcs = [];
            let medias = [];
            let variants = [];
            let characterTropeList = [];
            let characterPowerList = [];
            let characterStoryArcList = [];
            let characterMediaList = [];
            let characterVariantList = [];

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

            for (const [key, val] of Object.entries(this.powerData)) {
                powers.push(separateWordsByCapitalLetters(key));
                let belongsTo = val.belongsTo;
                let powerDescriptions = val.powerDescription;
                for (let i = 0; i < belongsTo.length; i++) {
                    let character = belongsTo[i];
                    let powerCharacterDescription = powerDescriptions[i];
                    characters.push(separateWordsByCapitalLetters(character));
                    characterPowerList.push({
                        character: separateWordsByCapitalLetters(character),
                        power: separateWordsByCapitalLetters(key),
                        description: powerCharacterDescription
                    });
                }
            }

            for (const [key, val] of Object.entries(this.storyArcData)) {
                storyArcs.push(separateWordsByCapitalLetters(key));
                let belongsTo = val.belongsTo;
                let storyArcDescriptions = val.storyDescription;
                for (let i = 0; i < belongsTo.length; i++) {
                    let character = belongsTo[i];
                    let storyArcCharacterDescription = storyArcDescriptions[i];
                    characters.push(separateWordsByCapitalLetters(character));
                    characterStoryArcList.push({
                        character: separateWordsByCapitalLetters(character),
                        storyArc: separateWordsByCapitalLetters(key),
                        description: storyArcCharacterDescription
                    });
                }
            }

            for (const [key, val] of Object.entries(this.variantData)) {
                variants.push(separateWordsByCapitalLetters(key));
                let belongsTo = val.belongsTo;
                let alternateVersionsDescriptions = val.alternateVersionsDescription;
                for (let i = 0; i < belongsTo.length; i++) {
                    let character = belongsTo[i];
                    let variantCharacterDescription = alternateVersionsDescriptions[i];
                    characters.push(separateWordsByCapitalLetters(character));
                    characterVariantList.push({
                        character: separateWordsByCapitalLetters(character),
                        variant : separateWordsByCapitalLetters(key),
                        description: variantCharacterDescription
                    });
                }
            }


            for (const [key, val] of Object.entries(this.mediaData)) {
                medias.push({
                    id: separateWordsByCapitalLetters(key),
                    media: val.mediaType[0]
                });
                let belongsTo = val.belongsTo;
                let mediaDescriptions = val.mediaDescription;
                for (let i = 0; i < belongsTo.length; i++) {
                    let character = belongsTo[i];
                    let mediaCharacterDescription = mediaDescriptions[i];
                    characters.push(separateWordsByCapitalLetters(character));
                    characterMediaList.push({
                        character: separateWordsByCapitalLetters(character),
                        media: separateWordsByCapitalLetters(key),
                        description: mediaCharacterDescription
                    });
                }
            }

            // Make into a set
            characters = [...new Set(characters)]

            let tropeNodes = [];
            let characterNodes = [];
            let powerNodes = [];
            let storyArcNodes = [];
            let mediaNodes = [];
            let variantNodes = [];
            let tropeEdges = [];
            let powerEdges = [];
            let storyArcEdges = [];
            let mediaEdges = [];
            let variantEdges = [];

            for (let i = 0; i < tropes.length; i++) {
                tropeNodes.push({
                    data: {
                        id: tropes[i],
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

            for (let i = 0; i < powers.length; i++) {
                powerNodes.push({
                    data: {
                        id: powers[i]
                    },
                    classes: ['power']
                });
            }

            for (let i = 0; i < storyArcs.length; i++) {
                storyArcNodes.push({
                    data: {
                        id: storyArcs[i]
                    },
                    classes: ['storyArc']
                });
            }

            for (let i = 0; i < variants.length; i++) {
                variantNodes.push({
                    data: {
                        id: variants[i]
                    },
                    classes: ['variant']
                });
            }

            for (let i = 0; i < medias.length; i++) {
                mediaNodes.push({
                    data: {
                        id: medias[i].id,
                        label: `${medias[i].id} (${medias[i].media})`
                    },
                    classes: ['media']
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

            for (let i = 0; i < characterPowerList.length; i++) {
                powerEdges.push({
                    data: {
                        id: `${characterPowerList[i].character}-${characterPowerList[i].power}`,
                        source: characterPowerList[i].character,
                        target: characterPowerList[i].power,
                        label: characterPowerList[i].description
                    }
                });
            }

            for (let i = 0; i < characterStoryArcList.length; i++) {
                storyArcEdges.push({
                    data: {
                        id: `${characterStoryArcList[i].character}-${characterStoryArcList[i].storyArc}`,
                        source: characterStoryArcList[i].character,
                        target: characterStoryArcList[i].storyArc,
                        label: characterStoryArcList[i].description
                    }
                });
            }

            for (let i = 0; i < characterVariantList.length; i++) {
                variantEdges.push({
                    data: {
                        id: `${characterVariantList[i].character}-${characterVariantList[i].variant}`,
                        source: characterVariantList[i].character,
                        target: characterVariantList[i].variant,
                        label: characterVariantList[i].description
                    }
                });
            }

            for (let i = 0; i < characterMediaList.length; i++) {
                mediaEdges.push({
                    data: {
                        id: `${characterMediaList[i].character}-${characterMediaList[i].media}`,
                        source: characterMediaList[i].character,
                        target: characterMediaList[i].media,
                        label: characterMediaList[i].description
                    }
                });
            }


            let layoutBFSOptions = () => {
                return {
                    name: 'breadthfirst',
                    roots: this.selectedNode
                }
            }

            let layoutSpreadOptions = {
                name: 'spread',
                nodeRepulsion: node => {
                    if (node.hasClass('character')) {
                        // console.log("Node is character")
                        return 1000000
                    } else {
                        return 1000000
                    }

                }
            }

            this.cy = cytoscape({

                container: this.cyElem, // container to render in

                elements: {// list of graph elements to start with
                    nodes: [
                        ...characterNodes,
                        ...tropeNodes,
                        ...powerNodes,
                        ...storyArcNodes,
                        ...mediaNodes,
                        ...variantNodes
                    ],
                    edges: [
                        ...tropeEdges,
                        ...powerEdges,
                        ...storyArcEdges,
                        ...mediaEdges,
                        ...variantEdges
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
                        selector: '.power',
                        style: {
                            'background-color': 'rgba(255,255,0,1)',
                            'label': 'data(id)'
                        }
                    },
                    {
                        selector: '.storyArc',
                        style: {
                            'background-color': 'rgba(255,0,0,1)',
                            'label': 'data(id)'
                        }
                    },
                    {
                        selector: '.media',
                        style: {
                            'background-color': 'rgba(0,0,255,1)',
                            'label': 'data(label)'
                        }
                    },
                    {
                        selector: '.variant',
                        style: {
                            'background-color': 'rgba(255,0,255,1)',
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

                layout: layoutSpreadOptions
            })

            this.cy.on('tap', 'edge', evt => {
                var edge = evt.target;
                let label = edge.data('label');
                this.selectedDescription = label;
                this.selectedDescriptionTrope = edge.data('target');
                this.selectedDescriptionCharacter = edge.data('source');
                this.selectedNode = null;
                this.$forceUpdate();
            });



            this.cy.on('tap', 'node', evt => {
                var node = evt.target;
                this.selectedDescription = null;
                if (this.selectedNode != node) {
                    // Selecting one or another
                    this.selectedNode = node;
                    this.cy.layout(layoutBFSOptions()).run();
                }
                else {
                    // Deselecting
                    this.selectedNode = null;
                    this.cy.layout(layoutSpreadOptions).run();
                }
                this.$forceUpdate()

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

                //layout: layoutSpreadOptions
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

            this.cy.on('tap', 'edge', evt => {
                var edge = evt.target;
                let label = edge.data('label');
                this.selectedDescription = label;
                this.$forceUpdate();
            });



            this.cy.on('tap', 'node', evt => {
                var node = evt.target;
                if (this.selectedNode != node) {
                    // Selecting one or another
                    this.selectedNode = node;
                    cy.layout(layoutBFSOptions()).run();
                }
                else {
                    // Deselecting
                    cy.layout(layoutSpreadOptions).run();
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
        this.cyElem = document.getElementById('cy')
        let checkboxes = document.querySelectorAll('input[type=checkbox]')
        for (let i = 0; i < checkboxes.length; i++) {
            checkboxes[i].addEventListener('change', (e) => {
                this.updateVisibleNodes(e);
            })
        }
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