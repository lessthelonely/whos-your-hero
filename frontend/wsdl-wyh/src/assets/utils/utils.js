
export function separateWordsByCapitalLetters(inputString) {
    if(inputString == "Deadpool22018"){
      return "Deadpool 2 2018";
    }
    if (inputString == "HeroicBSoD") {
      return "Heroic BSoD";
    }
    if (inputString == "MoreHerothanThou") {
      return "More Hero than Thou";
    }
    if (inputString == "BatmanGrabsaGun") {
      return "Batman Grabs a Gun";
    }
    if (inputString == "JerkassHasaPoint") {
      return "Jerkass Has a Point";
    }
  
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
      if(wordsArray[i].includes("is") && wordsArray[i] != "Analysis" && wordsArray[i] != "Genesis" && wordsArray[i] != "Regenesis" && wordsArray[i] != "Orchis" && wordsArray[i] != "This" && wordsArray[i] != "His"){
            var index = wordsArray[i].indexOf("is");
            var nextIndex = index + "is".length;
            if(nextIndex == wordsArray[i].length){
              wordsArray[i] = wordsArray[i].replace("is", " is");
            }
          }
      if(wordsArray[i].includes("or") && wordsArray[i] != "Junior" && wordsArray[i] != "Mentor" && wordsArray[i] != "Fervor" && wordsArray[i] != "Survivor" && wordsArray[i] != "Terror" && wordsArray[i] != "Liquor" && wordsArray[i] != "Minor" && wordsArray[i] != "Warrior" && wordsArray[i] != "Major" && wordsArray[i] != "Humor" && wordsArray[i] != "Motor" && wordsArray[i] != "Visor" && wordsArray[i] != "Pryor" && wordsArray[i] != "Factor" && wordsArray[i] != "Color" && wordsArray[i] != "Armor" && wordsArray[i] != "Determinator" && wordsArray[i] != "Poor" && wordsArray[i] != "Error" && !(wordsArray[i].includes("for"))){
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
      if(wordsArray[i].includes("a") && !(wordsArray[i].includes("on") || wordsArray[i].includes("of")) && wordsArray[i] != "Alpha" && wordsArray[i] != "Myopia" && wordsArray[i] != "Kotobukiya" && wordsArray[i] != "Necrosha" && wordsArray[i] != "Insignia" && wordsArray[i] != "Ninja" && wordsArray[i] != "Aura" && wordsArray[i] != "Extra" && wordsArray[i] != "Emma" && wordsArray[i] != "Utopia" && wordsArray[i] != "Godzilla"){
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
      if (wordsArray[i].includes("and") && !(wordsArray[i].includes("the")) && (wordsArray[i] != "Grand") && (wordsArray[i] != "Hand") && wordsArray[i] != "Husband" && wordsArray[i] != "Stand") {
        var index = wordsArray[i].indexOf("and");
        var nextIndex = index + "and".length;
        if (nextIndex == wordsArray[i].length) {
          wordsArray[i] = wordsArray[i].replace("and", " and");
        }
      }
      if (wordsArray[i].includes("by") && !(wordsArray[i].includes("Baby")) && !(wordsArray[i].includes("Ruby"))) {
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
      if(wordsArray[i].includes("an") && wordsArray[i] != "Man" && wordsArray[i] != "Logan" && wordsArray[i] != "Batman" && wordsArray[i] != "Human" && wordsArray[i] != "Gunman" && wordsArray[i] != "Amazonian" && wordsArray[i] != "Spartan" && wordsArray[i] != "Deadpan" && wordsArray[i] != "Superhuman" && wordsArray[i] != "Superman" && wordsArray[i] != "Than" && wordsArray[i] != "Freudian" && wordsArray[i] != "Can" && wordsArray[i] != "Technician" && wordsArray[i] != "Jean" && wordsArray[i] != "Nathan" && wordsArray[i] != "Barbarian" && wordsArray[i] != "Inhuman" && wordsArray[i] != "Totalitarian"  && wordsArray[i] != "Utilitarian" && !(wordsArray[i].includes("than"))){
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
      if(wordsArray[i].includes("at") && wordsArray[i] != "Bat" && !(wordsArray[i].includes("What")) && wordsArray[i] != "Combat" && wordsArray[i] != "That" && wordsArray[i] != "Copycat" && wordsArray[i] != "Kombat" && wordsArray[i] != "Coat" && wordsArray[i] != "Cat" && wordsArray[i] != "Great"){
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