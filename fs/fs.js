/*
Code disponible sous licence GPL v. 3.0
Cf. https://www.gnu.org/licenses/gpl-3.0.fr.html

Script d'aide à la correction d'OCR des f en ſ

    Copyright (C) 2020 Philippe Gambette

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

var treatedWords = 0

// Treat each HTML block with the line class
$(document).ready( function() {
  $(".line").each(
     function(index) {
        $(this).html( treat( $(this).html() ) );
     }
  );
})


// Replace by an ſ, in word, each s which was originally an f in replacedWord 
function restoreLongS(word,replacedWord){
   var i = 0;
   var outputWord = "";
   console.log(word[i],replacedWord[i]);
   while(i<word.length){
     if(replacedWord[i] == "f" && word[i] == "s"){
        outputWord += "ſ";
     } else {
        outputWord += word[i];
     }
     i++;
   }
   console.log(outputWord);
   return outputWord;
}


// Color the word if it was corrected or corresponds to an ambiguity
function treatWord(word){
   if (dictionary.hasOwnProperty(word)) {
      // if the word is found in the list of words to correct, pssibly
      //console.log(word)
      var correction = dictionary[word];
      if(correction.length == 1){
         // if there is no ambiguity, correct the word
         word = "<span class=\"replaced\">"+restoreLongS(correction[0],word)+"</span>";
      }else{
         // if there is an ambiguity, keep the original word
         word = "<span class=\"candidate\">"+word+"</span>";
      } 
   }
   return word;
}


// 
function treat(line){
   var output = "";
   var currentWord = "";
   var foundHtmlTag = false;
   var foundHtmlSpecialChar = false;  
   var lastCharacterIsPunctuation = false;
   var punct = [" ",",",".","'","-",";","?","!",":","’"," ","\n","\r"];
   for (var i = 0, len = line.length; i < len; i++) {
      if (line[i] == "<") {
         //If we find the beginning of an HTML tag, do not modify it
         foundHtmlTag = true;
         if (currentWord.length > 0) {
            output += treatWord(currentWord);
         }
         currentWord = "<";
      } else {
         if (line[i] == ">") {
            //If we reach the end of a tag, simply add the tag to the output and start a new current word
            foundHtmlTag = false;
            output += currentWord+">";
            currentWord = "";
         } else {
            if ((!foundHtmlTag) && (line[i] == "&")) {
               //If we find the beginning of an HTML special char, do not modify it
               foundHtmlSpecialChar = true;
               if (currentWord.length > 0) {
                  output += treatWord(currentWord);
               }
               currentWord = "&";
            } else {
               if ((foundHtmlSpecialChar) && (line[i] == ";")) {
                  //If we reach the end of an html special char, simply add the tag to the output and start a new current word
                  foundHtmlSpecialChar = false;
                  output += currentWord+";";
                  currentWord = "";
               } else {
               //Check if the current character is punctuation
                  if ((!foundHtmlTag) && (!foundHtmlSpecialChar) && (punct.includes(line[i]))) {
                     if(currentWord.length > 0){
                        output += treatWord(currentWord);
                     }
                     output += line[i]
                     lastCharacterIsPunctuation = true;
                     currentWord = "";
                  } else {
                     lastCharacterIsPunctuation = false;
                     currentWord += line[i];
                  }
               }
            }
         }
      }
   }
   if (!lastCharacterIsPunctuation) {
      output += treatWord(currentWord);
   }
   //console.log(output);
   return output;
}
