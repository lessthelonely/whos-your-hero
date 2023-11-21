<template>
  <h1>

  </h1>
</template>

<script>
import { defineComponent } from 'vue'
import axios from 'axios'

export default defineComponent({
  data() {
    return {
      id: String,
      name: String
    }
  },

  async beforeMount() {
    this.id = this.$route.params.id

    this.name = '';
    
    var count = 0
    for (var n in this.id.replace('_', ' ').split(' ')) {
      this.name += n[0].toUpperCase() + n.slice(1)

      if (count == this.id.replace('_', ' ').split(' ').length - 1)
        this.name += ' '
    }

    var characterData = {}

    await axios.get("http://localhost:8000/rdf-character/" + this.id)
      .then(response => {
        characterData = response.data
        console.log(response.data)
      });

      //Processing json data - put this wherever it's best for you
      var characterName = ""
      if(this.id == "cassandra_cain"){
        characterName = "CassandraCain";
      }
      else if(this.id == "emma_frost"){
        characterName = "EmmaFrost";
      }
      else if(this.id == "wally_west"){
        characterName = "WallyWest";
      }
      else if(this.id == "deadpool"){
        characterName = "Deadpool";
      }
      else{
        characterName = "Midnighter";
      }

      var uri = "http://whosyourhero.com/heroes.owl#" + characterName;

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

      console.log(birthday);

      //Get characterType
      var characterType = ""
      if(JSON.stringify(characterData["characterType"]) != "{}"){
        characterType = characterData["characterType"][uri][0];
      }
      else{
        characterType = "Unknown";
      }

      console.log(characterType);

      //Get number of issues that character appears in
      var numberOfIssues = ""
      if(JSON.stringify(characterData["appearsIn"]) != "{}"){
        numberOfIssues = characterData["appearsIn"][uri][0];
      }
      else{
        numberOfIssues = "Unknown";
      }

      console.log(numberOfIssues);

      //Get evolution
      var evolution = ""
      if(JSON.stringify(characterData["evolution"]) != "{}"){
        evolution = characterData["evolution"][uri][0];
      }
      else{
        evolution = "Unknown";
      }

      console.log(evolution);

      //Get creation
      var creation = ""
      if(JSON.stringify(characterData["creation"]) != "{}"){
        creation = characterData["creation"][uri][0];
      }
      else{
        creation = "Unknown";
      }

      console.log(creation);

      //Get creators
      var creators = ""
      if(JSON.stringify(characterData["creators"]) != "{}"){
        creators = characterData["creators"][uri][0];
      }
      else{
        creators = "Unknown";
      }

      console.log(creators);

      //Get deaths
      var deaths = ""
      if(JSON.stringify(characterData["deaths"]) != "{}"){
        deaths = characterData["deaths"][uri][0];
      }
      else{
        deaths = "Unknown";
      }

      console.log(deaths);

      //Get origins
      var origins = ""
      if(JSON.stringify(characterData["origins"]) != "{}"){
        origins = characterData["origins"][uri][0];
      }
      else{
        origins = "Unknown";
      }

      console.log(origins);

      //Get characteristics
      var characteristics = [];
      if(JSON.stringify(characterData["characteristics"]) != "{}"){
        characteristics = characterData["characteristics"][uri];
      }

      console.log(characteristics);

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
      console.log(characteristicsTypes);
      console.log(characteristicsDescriptions);


      //Get publisher
      var publisher = ""
      if(JSON.stringify(characterData["publisher"]) != "{}"){
        publisher = characterData["publisher"][uri][0];
      }
      else{
        publisher = "Unknown";
      }

      console.log(publisher);

      //Get real name
      var realName = ""
      if(JSON.stringify(characterData["realName"]) != "{}"){
        realName = characterData["realName"][uri][0];
      }
      else{
        realName = "Unknown";
      }

      console.log(realName);

      //Get summary
      var summary = ""
      if(JSON.stringify(characterData["summary"]) != "{}"){
        summary = characterData["summary"][uri][0];
      }
      else{
        summary = "Unknown";
      }

      console.log(summary);

      //Get super name
      var superName = ""
      if(JSON.stringify(characterData["superName"]) != "{}"){
        superName = characterData["superName"][uri][0];
      }
      else{
        superName = "Unknown";
      }

      console.log(superName);

      //Get first appearance
      var firstAppearance = ""
      if(JSON.stringify(characterData["firstAppearance"]) != "{}"){
        firstAppearance = characterData["firstAppearance"][uri][0];
      }
      else{
        firstAppearance = "Unknown";
      }

      console.log(firstAppearance);

      //Get alias
      var alias = []
      if(JSON.stringify(characterData["alias"]) != "{}"){
        alias = characterData["alias"][uri];
      }

      console.log(alias);

      //Get alternate Versions
      var alternateVersions = []
      if(JSON.stringify(characterData["alternateVersions"]) != "{}"){
        alternateVersions = characterData["alternateVersions"];
        var alternateVersionsTypes = Object.keys(characterData["alternateVersions"]);
        var alternateVersionsDescriptions = Object.values(characterData["alternateVersions"]);

        console.log(alternateVersions);
        console.log(alternateVersionsTypes);
        console.log(alternateVersionsDescriptions);

      }

      //Get storyArcs
      var storyArcs = []
      if(JSON.stringify(characterData["storyArcs"]) != "{}"){
        storyArcs = characterData["storyArcs"];
        var storyArcsTypes = Object.keys(characterData["storyArcs"]);
        var storyArcsDescriptions = Object.values(characterData["storyArcs"]);

        console.log(storyArcs);
        console.log(storyArcsTypes);
        console.log(storyArcsDescriptions);
      }

      //Get powers
      var powers = []
      if(JSON.stringify(characterData["powers"]) != "{}"){
        powers = characterData["powers"];
        var powersTypes = Object.keys(characterData["powers"]);
        var powersDescriptions = Object.values(characterData["powers"]);

        console.log(powers);
        console.log(powersTypes);
        console.log(powersDescriptions);
      }

      //Get tropes
      var tropes = []
      if(JSON.stringify(characterData["tropes"]) != "{}"){
        tropes = characterData["tropes"];
        var tropesTypes = Object.keys(characterData["tropes"]);
        var tropesDescriptions = Object.values(characterData["tropes"]);

        console.log(tropes);
        console.log(tropesTypes);
        console.log(tropesDescriptions);
      }

      //Get media
      var media = []
      var mediaTypes = [];
      var mediaDescriptions = [];
      if(JSON.stringify(characterData["media"]) != "{}"){
        media = characterData["media"];
        var mediaTitles = Object.keys(characterData["media"]);
        var mediaTypesDescriptions = Object.values(characterData["media"]);

        for (var i = 0; i < mediaTitles.length; i++) {
          mediaTypes.push(mediaTypesDescriptions[i]["mediaType"]);
          mediaDescriptions.push(mediaTypesDescriptions[i]["mediaDescription"]);
        }
        console.log(media);
        console.log(mediaTitles);
        console.log(mediaTypes);
        console.log(mediaDescriptions);
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

      console.log(isWoman);

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
  }
})
</script>

