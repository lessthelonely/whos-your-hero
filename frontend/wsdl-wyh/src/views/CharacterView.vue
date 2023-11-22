<template>
  <h1>

  </h1>
</template>

<script>
import { defineComponent } from 'vue'
import axios from 'axios'
import { Character } from '../stores/Character.js'

function separateWordsByCapitalLetters(inputString) {
    // Use a regular expression to split the string at capital letters
    inputString = inputString.replace(/_/g, ' ');
    
    // Use a regular expression to split the string at specific patterns
    var wordsArray = inputString.split(/(?<=[^\/A-Z])(?=[A-Z]|$)/);
  
    for(var i = 0; i < wordsArray.length; i++){
      if(wordsArray[i].includes("andthe")){
        wordsArray[i] = wordsArray[i].replace("andthe", "and the");
      }
      if(wordsArray[i].includes("and")){
        wordsArray[i] = wordsArray[i].replace("and", " and");
      }
      //vs, the, onthe, on, a (ARealManIsaKiller), ona (PutonaBus), to, of -> be careful: need more time to think about it
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
      if(JSON.stringify(characterData["photo"]) != "{}"){
        photo = characterData["photo"][uri][0];
      }
      else{
        this.photo = "https://www.pngitem.com/pimgs/m/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png";
      }

      console.log(photo);

      //Get birthday
      var birthday = ""
      if(JSON.stringify(characterData["birthday"]) != "{}"){
        birthday = characterData["birthday"][uri][0];
      }
      else{
        birthday = "Unknown";
      }

      //console.log(birthday);

      //Get characterType
      var characterType = ""
      if(JSON.stringify(characterData["characterType"]) != "{}"){
        characterType = characterData["characterType"][uri][0];
      }
      else{
        characterType = "Unknown";
      }

      //console.log(characterType);

      //Get number of issues that character appears in
      var numberOfIssues = ""
      if(JSON.stringify(characterData["appearsIn"]) != "{}"){
        numberOfIssues = characterData["appearsIn"][uri][0];
      }
      else{
        numberOfIssues = "Unknown";
      }

      //console.log(numberOfIssues);

      //Get evolution
      var evolution = ""
      if(JSON.stringify(characterData["evolution"]) != "{}"){
        evolution = characterData["evolution"][uri][0];
      }
      else{
        evolution = "Unknown";
      }

      //console.log(evolution);

      //Get creation
      var creation = ""
      if(JSON.stringify(characterData["creation"]) != "{}"){
        creation = characterData["creation"][uri][0];
      }
      else{
        creation = "Unknown";
      }

      //console.log(creation);

      //Get creators
      var creators = ""
      if(JSON.stringify(characterData["creators"]) != "{}"){
        creators = characterData["creators"][uri][0];
      }
      else{
        creators = "Unknown";
      }

      //console.log(creators);

      //Get deaths
      var deaths = ""
      if(JSON.stringify(characterData["deaths"]) != "{}"){
        deaths = characterData["deaths"][uri][0];
      }
      else{
        deaths = "Unknown";
      }

      //console.log(deaths);

      //Get origins
      var origins = ""
      if(JSON.stringify(characterData["origins"]) != "{}"){
        origins = characterData["origins"][uri][0];
      }
      else{
        origins = "Unknown";
      }

      //console.log(origins);

      //Get characteristics
      var characteristics = [];
      var characteristicsDict = {};
      if(JSON.stringify(characterData["characteristics"]) != "{}"){
        characteristics = characterData["characteristics"][uri];
      }

      //console.log(characteristics);

      var characteristicsTypes = []
      var characteristicsDescriptions = [];
      for(var i = 0; i < characteristics.length; i++){
        var characteristic = characteristics[i].split(":");
        characteristicsTypes.push(characteristic[0]);
        var characteristicDescription = ""
        if(characteristic[1][0] == " "){
          characteristicDescription = characteristic[1].slice(1);
        }
        else{
          characteristicDescription = characteristic[1];
        }
        characteristicsDescriptions.push(characteristicDescription);
      }

      for (var i = 0; i < characteristicsTypes.length; i++) {
        characteristicsDict[characteristicsTypes[i]] = characteristicsDescriptions[i];
      }

      //Get publisher
      var publisher = ""
      if(JSON.stringify(characterData["publisher"]) != "{}"){
        publisher = characterData["publisher"][uri][0];
      }
      else{
        publisher = "Unknown";
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

      //Get isWoman
      var isWoman = false
      if(JSON.stringify(characterData["isWoman"]) != "{}"){
        isWoman = characterData["isWoman"][uri][0];
        if(isWoman == "true"){
          isWoman = true;
        }
        else{
          isWoman = false;
        }
      }

      //Get isMan
      var isMan = false
      if(JSON.stringify(characterData["isMan"]) != "{}"){
        isMan = characterData["isMan"][uri][0];
        if(isMan == "true"){
          isMan = true;
        }
        else{
          isMan = false;
        }
      }

      //Get isNonBinary
      var isNonBinary = false
      if(JSON.stringify(characterData["isNonBinary"]) != "{}"){
        isNonBinary = characterData["isNonBinary"][uri][0];
        if(isNonBinary == "true"){
          isNonBinary = true;
        }
        else{
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