<template>
  <h1>

  </h1>
</template>

<script>
import { defineComponent } from 'vue'
import axios from 'axios'
import { Character } from '../stores/Character.js'

    //vs, the, onthe, to, of -> be careful: need more time to think about it
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
      var alternateVersions = []
      var alternateVersionsDict = {};
      if(JSON.stringify(characterData["alternateVersions"]) != "{}"){
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
      if(JSON.stringify(characterData["storyArcs"]) != "{}"){
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
      if(JSON.stringify(characterData["powers"]) != "{}"){
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
      if(JSON.stringify(characterData["tropes"]) != "{}"){
        tropes = characterData["tropes"];
        var tropesTypes = Object.keys(characterData["tropes"]);
        var tropesDescriptions = Object.values(characterData["tropes"]);
      }

      for (var i = 0; i < tropesTypes.length; i++) {
        tropesDict[tropesTypes[i]] = tropesDescriptions[i];
      }

      //Get media
      var media = []
      var mediaTypes = [];
      var mediaDescriptions = [];
      var mediaDict = {};
      if(JSON.stringify(characterData["media"]) != "{}"){
        media = characterData["media"];
        var mediaTitles = Object.keys(characterData["media"]);
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

      for (var i = 0; i < mediaTitles.length; i++) {
        mediaDict[mediaTitles[i]] = {
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

