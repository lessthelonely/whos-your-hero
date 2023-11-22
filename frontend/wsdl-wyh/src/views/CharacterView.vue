<template>
  <div style="display: flex;">
    <div class="col-md-7" style="width: 70%;">
      <div class="header">
        <h1 style="font-weight: bold;">
          {{ character.name }}
        </h1>
        <h6 style="font-style: italic;">
          {{ character.characterType }}
        </h6>
      </div>

      <div class="body" style="text-align: justify; padding-right: 30px;">
        <p class="summary">
          {{ character.summary }}
        </p>

        <div class="creation">
          <h5 style="margin-bottom: 5px;">
            Creation
          </h5>
          <p style="margin-top: 0px;">
            {{ character.creation }}
          </p>
        </div>

        <div class="origins">
          <h5 style="margin-bottom: 5px;">
            Origins
          </h5>
          <p style="margin-top: 0px;">
            {{ character.origins }}
          </p>
        </div>

        <div class="evolution">
          <h5 style="margin-bottom: 5px;">
            Evolution
          </h5>
          <p style="margin-top: 0px;">
            {{ character.evolution }}
          </p>
        </div>

        <div class="alternative-versions">
          <h5 style="margin-bottom: 12px;">
            Alternate Versions
          </h5>
          <div v-for="(altVerDes, altVerType) in character.alternateVersions" v-bind:key="altVerType.toString()"
            style="margin-bottom: 5px;">
            <h6 style="font-style: italic; margin-bottom: 5px;">
              {{ altVerType }}
            </h6>
            <p style="margin-top: 0px;">
              {{ altVerDes }}
            </p>
          </div>
        </div>

        <div class="powers">
          <h5 style="margin-bottom: 12px;">
            Powers
          </h5>
          <ul v-for="(powerDes, powerName) in character.powers" v-bind:key="powerName.toString()"
            style="margin-bottom: 5px;">
            <li style="margin-bottom: 5px;">
              <strong>{{ powerName.trim() }}</strong> {{ '- ' + powerDes }}
            </li>
          </ul>
        </div>

        <div class="story-arcs" style="margin-bottom: 10px;">
          <h5 style="margin-bottom: 12px;">
            Story Arcs
          </h5>
          <div v-for="(storyArcsDes, storyArcsType) in character.storyArcs" v-bind:key="storyArcsType.toString()"
            style="margin-bottom: 5px;">
            <h6 style="font-style: italic; margin-bottom: 5px;">
              {{ storyArcsType }}
            </h6>
            <p style="margin-top: 0px;">
              {{ storyArcsDes }}
            </p>
          </div>
        </div>

        <div class="tropes" style="margin-bottom: 15px;">
          <h5 style="margin-bottom: 12px;">
            Tropes
          </h5>
          <ul v-for="(tropeDes, tropeName) in character.tropes" v-bind:key="tropeName.toString()"
            style="margin-bottom: 5px;">
            <li style="margin-bottom: 5px;">
              <em>{{ tropeName.trim() }}</em> {{ '- ' + tropeDes.trim() }}
            </li>
          </ul>
        </div>

        <div class="media">
          <h5 style="margin-bottom: 12px;">
            Media
          </h5>    
          <div class="accordion-item" v-for="(mediaObj, mediaTitle) in character.media" v-bind:key="mediaTitle">
            <div>
              <h6 style="border-radius: 10px 10px 0px 0px; margin: 0px; background-color: #212529; color: white; padding: 5px;">
                {{ mediaTitle }}
              </h6>
              <h6 style="font-size: 14px; font-style: italic; background-color: #343a40; color: white; padding: 5px; margin: 0px;">
                {{ mediaObj.type }}
              </h6>
            </div>
            <p style="background-color: #adb5bd; padding: 5px; border-radius: 0px 0px 10px 10px;">
              {{ mediaObj.description }}
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="col-md-3" style="width: 30%; justify-content: center;">
      <table class="table table-dark">
        <thead colspan="2">
          <th colspan="2">
            <h3 style="font-weight: bold; text-align: center; margin-bottom: 0px;">
              General Information
            </h3>

            <h6 style="font-style: italic; text-align: center; margin-bottom: 0px;">
              {{ character.name }}
            </h6>

            <img :src="character.photo"
              style="width: 100%; height: 250px; padding: 0px; object-fit: cover; object-position: center top;" />
          </th>
        </thead>
        <tbody>
          <tr style="width: 100%" colspan="2">
            <td style="font-weight: bold;" scope="col">
              {{ "Birthday" }}
            </td>
            <td class="table-secondary" style="font-size: 15px; padding: 0px;" scope="col">
              <ul class="list-group list-group-flush">
                <li class="list-group-item list-group-item-secondary">
                  {{ character.birthday }}
                </li>
              </ul>
            </td>
          </tr>
          <tr style="width: 100%" colspan="2">
            <td style="font-weight: bold;" scope="col">
              {{ "Number of Issues" }}
            </td>
            <td class="table-secondary" style="font-size: 15px; padding: 0px;" scope="col">
              <ul class="list-group list-group-flush">
                <li class="list-group-item list-group-item-secondary">
                  {{ character.numberOfIssues }}
                </li>
              </ul>
            </td>
          </tr>
          <tr style="width: 100%" colspan="2">
            <td style="font-weight: bold;" scope="col">
              {{ "Real Name" }}
            </td>
            <td class="table-secondary" style="font-size: 15px; padding: 0px;" scope="col">
              <ul class="list-group list-group-flush">
                <li class="list-group-item list-group-item-secondary">
                  {{ character.realName }}
                </li>
              </ul>
            </td>
          </tr>
          <tr style="width: 100%" colspan="2">
            <td style="font-weight: bold;" scope="col">
              {{ "Super Name" }}
            </td>
            <td class="table-secondary" style="font-size: 15px; padding: 0px;" scope="col">
              <ul class="list-group list-group-flush">
                <li class="list-group-item list-group-item-secondary">
                  {{ character.superName }}
                </li>
              </ul>
            </td>
          </tr>
          <tr style="width: 100%" colspan="2">
            <td style="font-weight: bold;" scope="col">
              {{ "Aliases" }}
            </td>
            <td class="table-secondary" style="font-size: 15px; padding: 0px;" scope="col">
              <ul class="list-group list-group-flush">
                <li class="list-group-item list-group-item-secondary" v-for="a in character.alias" v-bind:key="a">
                  {{ a }}
                </li>
              </ul>
            </td>
          </tr>
          <tr style="width: 100%" colspan="2">
            <td style="font-weight: bold;" scope="col">
              {{ "First Appearance" }}
            </td>
            <td class="table-secondary" style="font-size: 15px; padding: 0px;" scope="col">
              <ul class="list-group list-group-flush">
                <li class="list-group-item list-group-item-secondary" style="font-style: italic;">
                  {{ character.firstAppearance }}
                </li>
              </ul>
            </td>
          </tr>
          <tr style="width: 100%" colspan="2">
            <td style="font-weight: bold;" scope="col">
              {{ "Creator(s)" }}
            </td>
            <td class="table-secondary" style="font-size: 15px; padding: 0px;" scope="col">
              <ul class="list-group list-group-flush">
                <li class="list-group-item list-group-item-secondary">
                  {{ character.creators }}
                </li>
              </ul>
            </td>
          </tr>
          <tr style="width: 100%" colspan="2">
            <td style="font-weight: bold;" scope="col">
              {{ "Publisher" }}
            </td>
            <td class="table-secondary" style="font-size: 15px; padding: 0px;" scope="col">
              <ul class="list-group list-group-flush">
                <li class="list-group-item list-group-item-secondary">
                  {{ character.publisher }}
                </li>
              </ul>
            </td>
          </tr>
          <tr colspan="2" class="table-dark" style="margin: 0px; padding: 0px;">
            <td colspan="2">

              <h6 style="font-weight: bold; text-align: center; margin-bottom: 0px;">
                Characteristics
              </h6>
            </td>
          </tr>
          <tr style="width: 100%" colspan="2">
            <td style="font-weight: bold;" scope="col">
              {{ "Gender" }}
            </td>
            <td class="table-secondary" style="font-size: 15px; padding: 0px;" scope="col">
              <ul class="list-group list-group-flush">
                <li class="list-group-item list-group-item-secondary">
                  {{ character.gender }}
                </li>
              </ul>
            </td>
          </tr>
          <tr style="width: 100%" v-for="(key, value) in character.characteristics" v-bind:key="key" colspan="2">
            <td style="font-weight: bold;" scope="col">
              {{ value }}
            </td>
            <td class="table-secondary" v-if="isSimple(value)" style="font-size: 15px; padding: 0px;" scope="col">
              <ul class="list-group list-group-flush">
                <li class="list-group-item list-group-item-secondary">
                  {{ key }}
                </li>
              </ul>
            </td>
            <td class="table-secondary" style="font-size: 14px; padding: 0px;" scope="col" v-else>
              <ul class="list-group list-group-flush">
                <li v-for="item in key.replace(';', ',').split(',')" v-bind:key="item.toString()"
                  class="list-group-item list-group-item-secondary">
                  {{ item }}
                </li>
              </ul>
            </td>
          </tr>
        </tbody>

      </table>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import axios from 'axios'
import { Character } from '../stores/Character.js'

//vs, the, onthe, to, of -> be careful: need more time to think about it
function getIndexOfNextCapitalLetter(inputString) {
    // Use a regular expression to split the string at capital letters
    var index = inputString.search(/[A-Z]/);
    return index;
  }

function separateWordsByCapitalLetters(inputString) {
    // Use a regular expression to split the string at capital letters
    inputString = inputString.replace(/_/g, ' ');
    //see about - 
    
    // Use a regular expression to split the string at specific patterns
    var wordsArray = inputString.split(/(?=[A-Z][a-z])|(?<=[a-z])(?=[A-Z])/);
  
    for(var i = 0; i < wordsArray.length; i++){
      if(wordsArray[i][wordsArray[i].length - 1] == "/" || wordsArray[i][wordsArray[i].length - 1] == "–"){
        wordsArray[i] = wordsArray[i] + wordsArray[i + 1];
        wordsArray.splice(i + 1, 1);
      }
      if(wordsArray[i].includes("andthe")){
        var index = wordsArray[i].indexOf("andthe");
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "andthe".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("andthe", " and the");
        }
      }
      if(wordsArray[i].includes("and") && !(wordsArray[i].includes("the"))){
        var index = wordsArray[i].indexOf("and");
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "and".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("and", " and");
        }
      }
      if(wordsArray[i].includes("ofa")){
        var index = wordsArray[i].indexOf("ofa");
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "ofa".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("ofa", " of a");
        }
      }
      if(wordsArray[i].includes("fromthe")){
        var index = wordsArray[i].indexOf("fromthe");
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "fromthe".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("fromthe", " from the");
        }
      }
      if(wordsArray[i].includes("ofthe")){
        var index = wordsArray[i].indexOf("ofthe");
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "ofthe".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("ofthe", " of the");
        }
      }
      if(wordsArray[i].includes("onthe")){
        var index = wordsArray[i].indexOf("onthe");
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "onthe".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("onthe", " on the");
        }
      }
      if(wordsArray[i].includes("tothe")){
        var index = wordsArray[i].indexOf("tothe");
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "tothe".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("tothe", " to the");
        }
      }
      if(wordsArray[i].includes("the") && !(wordsArray[i].includes("from") || wordsArray[i].includes("of") || wordsArray[i].includes("to") || wordsArray[i].includes("on"))){
        var index = wordsArray[i].indexOf("the");
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "the".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("the", " the");
        }
      }
      if(wordsArray[i].includes("ona")){
        var index = wordsArray[i].indexOf("ona"); 
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "ona".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("ona", " on a");
        }
      }
      /*if(wordsArray[i].includes("vs")){
        var index = wordsArray[i].indexOf("vs");
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "vs".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("vs", " vs");
        }
      }*/
      if(wordsArray[i].includes("of") && !(wordsArray[i].includes("a"))){
        var index = wordsArray[i].indexOf("of");
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "of".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("of", " of");
        }
      }
      if(wordsArray[i].includes("to")){
        var index = wordsArray[i].indexOf("to");
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "to".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("to", " to");
        }
      }
      if(wordsArray[i].includes("a") && !(wordsArray[i].includes("on") || wordsArray[i].includes("of"))){
        var index = wordsArray[i].indexOf("a");
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "a".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("a", " a");
        }
      }
      if(wordsArray[i].includes("by")){
        var index = wordsArray[i].indexOf("by");
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "by".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("by", " by");
        }
      }
      if(wordsArray[i].includes("but")){
        var index = wordsArray[i].indexOf("but");
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "but".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("but", " but");
        }
      }
      if(wordsArray[i].includes("with")){
        var index = wordsArray[i].indexOf("with");
        var nextCapitalLetterIndex = getIndexOfNextCapitalLetter(wordsArray[i].slice(index));
        var nextIndex = index + "with".length;
        if(nextCapitalLetterIndex == nextIndex || nextIndex == wordsArray[i].length){
          wordsArray[i] = wordsArray[i].replace("with", " with");
        }
      }
    }
  
    // Join the array elements with space to form the final string
    var resultString = wordsArray.join(' ');
  
    return resultString;
  }

export default defineComponent({
  data() {
    return {
      id: String,
      name: String,
      character: Character
    }
  },

  methods: {
    getName() {
      switch (this.id) {
        case "cassandra_cain":
          this.name = "Cassandra Cain"
          return "CassandraCain"
          break;
        case "emma_frost":
          this.name = "Emma Frost"
          return "EmmaFrost"
          break;
        case "wally_west":
          this.name = "Wally West"
          return "WallyWest"
          break;
        case "deadpool":
          this.name = "Deadpool"
          return "Deadpool"
          break;
        case "midnighter":
          this.name = "Midnighter"
          return "Midnighter"
          break;
        default:
          throw console.error("Character not found");
      }
    },

    isSimple(variable) {
      var simples = ["Place of Birth", "Education", "Height", "Weight", "Eyes", "Hair", "Distinguishing Features", "Identity"]
      return simples.includes(variable);
    }
  },

  async beforeMount() {
    this.id = this.$route.params.id

    var characterData = {}

    await axios.get("http://localhost:8000/rdf-character/" + this.id)
      .then(response => {
        characterData = response.data
        //console.log(response.data)
      });

    var uri = "http://whosyourhero.com/heroes.owl#" + this.getName();

    //Get photo
    var photo = ""
    if (JSON.stringify(characterData["photo"]) != "{}") {
      photo = characterData["photo"][uri][0];
    }
    else {
      this.photo = "https://www.pngitem.com/pimgs/m/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png";
    }

    console.log(photo);

    //Get birthday
    var birthday = ""
    if (JSON.stringify(characterData["birthday"]) != "{}") {
      birthday = characterData["birthday"][uri][0];
    }
    else {
      birthday = "Unknown";
    }

    //console.log(birthday);

    //Get characterType
    var characterType = ""
    if (JSON.stringify(characterData["characterType"]) != "{}") {
      characterType = characterData["characterType"][uri][0];
    }
    else {
      characterType = "Unknown";
    }

    //console.log(characterType);

    //Get number of issues that character appears in
    var numberOfIssues = ""
    if (JSON.stringify(characterData["appearsIn"]) != "{}") {
      numberOfIssues = characterData["appearsIn"][uri][0];
    }
    else {
      numberOfIssues = "Unknown";
    }

    //console.log(numberOfIssues);

    //Get evolution
    var evolution = ""
    if (JSON.stringify(characterData["evolution"]) != "{}") {
      evolution = characterData["evolution"][uri][0];
    }
    else {
      evolution = "Unknown";
    }

    //console.log(evolution);

    //Get creation
    var creation = ""
    if (JSON.stringify(characterData["creation"]) != "{}") {
      creation = characterData["creation"][uri][0];
    }
    else {
      creation = "Unknown";
    }

    //console.log(creation);

    //Get creators
    var creators = ""
    if (JSON.stringify(characterData["creators"]) != "{}") {
      creators = characterData["creators"][uri][0];
    }
    else {
      creators = "Unknown";
    }

    //console.log(creators);

    //Get deaths
    var deaths = ""
    if (JSON.stringify(characterData["deaths"]) != "{}") {
      deaths = characterData["deaths"][uri][0];
    }
    else {
      deaths = "Unknown";
    }

    //console.log(deaths);

    //Get origins
    var origins = ""
    if (JSON.stringify(characterData["origins"]) != "{}") {
      origins = characterData["origins"][uri][0];
    }
    else {
      origins = "Unknown";
    }

    //console.log(origins);

    //Get characteristics
    var characteristics = [];
    var characteristicsDict = {};
    if (JSON.stringify(characterData["characteristics"]) != "{}") {
      characteristics = characterData["characteristics"][uri];
    }

    //console.log(characteristics);

    var characteristicsTypes = []
    var characteristicsDescriptions = [];
    for (var i = 0; i < characteristics.length; i++) {
      var characteristic = characteristics[i].split(":");
      characteristicsTypes.push(characteristic[0]);
      var characteristicDescription = ""
      if (characteristic[1][0] == " ") {
        characteristicDescription = characteristic[1].slice(1);
      }
      else {
        characteristicDescription = characteristic[1];
      }
      characteristicsDescriptions.push(characteristicDescription);
    }

    for (var i = 0; i < characteristicsTypes.length; i++) {
      characteristicsDict[characteristicsTypes[i]] = characteristicsDescriptions[i];
    }

    //Get publisher
    var publisher = ""
    if (JSON.stringify(characterData["publisher"]) != "{}") {
      publisher = characterData["publisher"][uri][0];
    }
    else {
      publisher = "Unknown";
    }

    //console.log(publisher);

    //Get real name
    var realName = ""
    if (JSON.stringify(characterData["realName"]) != "{}") {
      realName = characterData["realName"][uri][0];
    }
    else {
      realName = "Unknown";
    }

    //console.log(realName);

    //Get summary
    var summary = ""
    if (JSON.stringify(characterData["summary"]) != "{}") {
      summary = characterData["summary"][uri][0];
    }
    else {
      summary = "Unknown";
    }

    //console.log(summary);

    //Get super name
    var superName = ""
    if (JSON.stringify(characterData["superName"]) != "{}") {
      superName = characterData["superName"][uri][0];
    }
    else {
      superName = "Unknown";
    }

    //console.log(superName);

    //Get first appearance
    var firstAppearance = ""
    if (JSON.stringify(characterData["firstAppearance"]) != "{}") {
      firstAppearance = characterData["firstAppearance"][uri][0];
    }
    else {
      firstAppearance = "Unknown";
    }

    //console.log(firstAppearance);

    //Get alias
    var alias = []
    if (JSON.stringify(characterData["alias"]) != "{}") {
      alias = characterData["alias"][uri];
    }

    //console.log(alias);

    //Get alternate Versions
    var alternateVersions = []
    var alternateVersionsDict = {};
    if (JSON.stringify(characterData["alternateVersions"]) != "{}") {
      alternateVersions = characterData["alternateVersions"];
      var alternateVersionsTypes = Object.keys(characterData["alternateVersions"]);
      var alternateVersionsDescriptions = Object.values(characterData["alternateVersions"]);

      //console.log(alternateVersions);
      //console.log(alternateVersionsTypes);
      //console.log(alternateVersionsDescriptions);
    }

    for (var i = 0; i < alternateVersionsTypes.length; i++) {
      alternateVersionsDict[alternateVersionsTypes[i]] = alternateVersionsDescriptions[i];
    }

    //Get storyArcs
    var storyArcs = []
    var storyArcsDict = {};
    if (JSON.stringify(characterData["storyArcs"]) != "{}") {
      storyArcs = characterData["storyArcs"];
      var storyArcsTypes = Object.keys(characterData["storyArcs"]);
      var storyArcsDescriptions = Object.values(characterData["storyArcs"]);
    }

    for (var i = 0; i < storyArcsTypes.length; i++) {
      storyArcsDict[storyArcsTypes[i]] = storyArcsDescriptions[i];
    }

    //Get powers
    var powers = []
    var powersDict = {};
    if (JSON.stringify(characterData["powers"]) != "{}") {
      powers = characterData["powers"];
      var powersTypes = Object.keys(characterData["powers"]);
      var powersDescriptions = Object.values(characterData["powers"]);
    }

    for (var i = 0; i < powersTypes.length; i++) {
      powersDict[powersTypes[i]] = powersDescriptions[i];
    }

    //Get tropes
    var tropes = []
    var tropesDict = {};
    if (JSON.stringify(characterData["tropes"]) != "{}") {
      tropes = characterData["tropes"];
      var tropesTypes = Object.keys(characterData["tropes"]);
      var tropesDescriptions = Object.values(characterData["tropes"]);
    }

    for (var i = 0; i < tropesTypes.length; i++) {
      tropesDict[tropesTypes[i]] = tropesDescriptions[i];
    }

      //console.log(publisher);

      //Get real name
      var realName = ""
      if(JSON.stringify(characterData["realName"]) != "{}"){
        realName = characterData["realName"][uri][0];
      }
      else{
        realName = "Unknown";
      }

      //console.log(realName);

      //Get summary
      var summary = ""
      if(JSON.stringify(characterData["summary"]) != "{}"){
        summary = characterData["summary"][uri][0];
      }
      else{
        summary = "Unknown";
      }

      //console.log(summary);

      //Get super name
      var superName = ""
      if(JSON.stringify(characterData["superName"]) != "{}"){
        superName = characterData["superName"][uri][0];
      }
      else{
        superName = "Unknown";
      }

      //console.log(superName);

      //Get first appearance
      var firstAppearance = ""
      if(JSON.stringify(characterData["firstAppearance"]) != "{}"){
        firstAppearance = characterData["firstAppearance"][uri][0];
      }
      else{
        firstAppearance = "Unknown";
      }

      //console.log(firstAppearance);

      //Get alias
      var alias = []
      if(JSON.stringify(characterData["alias"]) != "{}"){
        alias = characterData["alias"][uri];
      }

      //console.log(alias);

      //Get alternate Versions
      var alternateVersionsDict = {};
      if(JSON.stringify(characterData["alternateVersions"]) != "{}"){
        var alternateVersionsTypes = Object.keys(characterData["alternateVersions"]);

        var alternateVersionsTypesTreated = [];
          for (var i = 0; i < alternateVersionsTypes.length; i++) {
            var alternateVersionsType = separateWordsByCapitalLetters(alternateVersionsTypes[i]);
            alternateVersionsTypesTreated.push(alternateVersionsType);
          }

        var alternateVersionsDescriptions = Object.values(characterData["alternateVersions"]);

        //console.log(alternateVersions);
        //console.log(alternateVersionsTypes);
        //console.log(alternateVersionsDescriptions);
      }

      for (var i = 0; i < alternateVersionsTypesTreated.length; i++) {
        alternateVersionsDict[alternateVersionsTypesTreated[i]] = alternateVersionsDescriptions[i];
      }

      //Get storyArcs
      var storyArcsDict = {};
      if(JSON.stringify(characterData["storyArcs"]) != "{}"){
        var storyArcsTypes = Object.keys(characterData["storyArcs"]);
        var storyArcsDescriptions = Object.values(characterData["storyArcs"]);

        var storyArcsTypesTreated = [];
          for (var i = 0; i < storyArcsTypes.length; i++) {
            var storyArcType = separateWordsByCapitalLetters(storyArcsTypes[i]);
            storyArcsTypesTreated.push(storyArcType);
          }
      }

      for (var i = 0; i < storyArcsTypesTreated.length; i++) {
        storyArcsDict[storyArcsTypesTreated[i]] = storyArcsDescriptions[i];
      }

      //Get powers
      var powersDict = {};
      if(JSON.stringify(characterData["powers"]) != "{}"){
        var powersTypes = Object.keys(characterData["powers"]);
        var powersDescriptions = Object.values(characterData["powers"]);

        var powersTypesTreated = [];
          for (var i = 0; i < powersTypes.length; i++) {
            var powersType = separateWordsByCapitalLetters(powersTypes[i]);
            powersTypesTreated.push(powersType);
          }
      }

      for (var i = 0; i < powersTypesTreated.length; i++) {
        powersDict[powersTypesTreated[i]] = powersDescriptions[i];
      }

      //Get tropes
      var tropesDict = {};
      if(JSON.stringify(characterData["tropes"]) != "{}"){
        var tropesTypes = Object.keys(characterData["tropes"]);
        var tropesDescriptions = Object.values(characterData["tropes"]);

        var tropesTypesTreated = [];
          for (var i = 0; i < tropesTypes.length; i++) {
            var tropesType = separateWordsByCapitalLetters(tropesTypes[i]);
            tropesTypesTreated.push(tropesType);
          }
      }

      for (var i = 0; i < tropesTypesTreated.length; i++) {
        tropesDict[tropesTypesTreated[i]] = tropesDescriptions[i];
      }

      //Get media
      var mediaTypes = [];
      var mediaDescriptions = [];
      var mediaDict = {};
      if(JSON.stringify(characterData["media"]) != "{}"){
        var mediaTitles = Object.keys(characterData["media"]);

        var mediaTitlesTreated = [];
          for (var i = 0; i < mediaTitles.length; i++) {
            var mediaTitle = separateWordsByCapitalLetters(mediaTitles[i]);
            mediaTitlesTreated.push(mediaTitle);
          }

        var mediaTypesDescriptions = Object.values(characterData["media"]);

        for (var i = 0; i < mediaTitles.length; i++) {
          mediaTypes.push(mediaTypesDescriptions[i]["mediaType"]);
          mediaDescriptions.push(mediaTypesDescriptions[i]["mediaDescription"]);
        }
        //console.log(media);
        //console.log(mediaTitles);
        //console.log(mediaTypes);
        //console.log(mediaDescriptions);
      }

      for (var i = 0; i < mediaTitlesTreated.length; i++) {
        mediaDict[mediaTitlesTreated[i]] = {
          "type": mediaTypes[i], 
          "description": mediaDescriptions[i]
        };
      }
      //console.log(media);
      //console.log(mediaTitles);
      //console.log(mediaTypes);
      //console.log(mediaDescriptions);
    }

    for (var i = 0; i < mediaTitles.length; i++) {
      mediaDict[mediaTitles[i]] = {
        "type": mediaTypes[i],
        "description": mediaDescriptions[i]
      };
    }

    //Get isWoman
    var isWoman = false
    if (JSON.stringify(characterData["isWoman"]) != "{}") {
      isWoman = characterData["isWoman"][uri][0];
      if (isWoman == "true") {
        isWoman = true;
      }
      else {
        isWoman = false;
      }
    }

    //Get isMan
    var isMan = false
    if (JSON.stringify(characterData["isMan"]) != "{}") {
      isMan = characterData["isMan"][uri][0];
      if (isMan == "true") {
        isMan = true;
      }
      else {
        isMan = false;
      }
    }

    //Get isNonBinary
    var isNonBinary = false
    if (JSON.stringify(characterData["isNonBinary"]) != "{}") {
      isNonBinary = characterData["isNonBinary"][uri][0];
      if (isNonBinary == "true") {
        isNonBinary = true;
      }
      else {
        isNonBinary = false;
      }
    }

    var gender = (isMan ? "Man" : (isWoman ? "Woman" : (isNonBinary ? "Non-binary" : "Unknown")));

    this.character = new Character(uri, this.name,
      photo, birthday, characterType, numberOfIssues,
      evolution, creation, creators, deaths, origins,
      characteristicsDict, publisher, realName, summary,
      superName, firstAppearance, alias, alternateVersionsDict,
      storyArcsDict, powersDict, tropesDict, mediaDict, gender)

    console.log(this.character)
    //console.log(characterData);
    //Cassandra doesn't have evolution or origins
    //Midnighter doesn't have media or characteristics
    //Wally doesn't have creation or evolution
    //Emma, Deadpool and Wally don't have birthdays (it will be written as Unknown)
  }
})
</script>