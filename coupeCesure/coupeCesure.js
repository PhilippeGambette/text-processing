/*
Code disponible sous licence GPL v. 3.0
Cf. https://www.gnu.org/licenses/gpl-3.0.fr.html

Script de suppression automatique des césures

    Copyright (C) 2017-2020 Philippe Gambette

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

var punct = [" ",",",".","'","-",";","?","!",":","’"," ","\n","\r"];



// Treat each HTML block with the line class
$(document).ready( function() {
  console.log(cleanText($("#theText").html()));
  $("#theText").html(cleanText($("#theText").html()));
})

// output the first word of the string
function firstWord(string){
   var i=0;
   while(i<string.length && !(punct.includes(string[i]))){
      i+=1;      
   }
   return string.substring(0,i);
}


function splitNextLine(string){
   var i=0;
   // Look for the possible end of the word on the next line
   while((i<string.length) && (string[i]!=" ")){
      i+=1;      
   }
   // If the end of the word in the beginning of the next line is followed by : ! ? or ; 
   // bring this punctuation mark in the end of the current line
   if((string[i+1]==":") || (string[i+1]=="!") || (string[i+1]=="?") || (string[i+1]==";")){
      i+=2;
   }
   return [string.substring(0,i),string.substring(i,string.length)];
}

function cleanText(text){
   var textTable = text.split(/\r?\n/);
   var output = "";
   var i=0;
   // for all lines
   while(i<textTable.length-1){
      var line = textTable[i];

      // Look for the position j of - or — in the end of the line
      var j=-1;
      if((line.substring(line.length-1,line.length)=="-")||(line.substring(line.length-1,line.length)=="—")){
         j = line.length-2;
      }
      if((line.substring(line.length-2,line.length)=="- ")||(line.substring(line.length-2,line.length)=="— ")){
         j = line.length-3;
      }

      // Extract the last word of the line starting from the position of the last - or — and going left
      var lastWord = "";
      while(j>-1 && !(punct.includes(line.substring(j,j+1)))){
      //while(j>-1 && line.substring(j,j+1)!=" "){
         lastWord = line.substring(j,j+1)+lastWord;
         j=j-1;
      }
      
      // If a last word was found just before - or — 
      if(lastWord.length>0){
         // This is possibly the beginning of a word ending on the next line
         //console.log(lastWord)
         
         // Get the possible end of the word on the next line
         var nextWord = firstWord(textTable[i+1]);
         //alert("["+lastWord+nextWord+"]")
         
         if(dico.includes(lastWord+nextWord)){
            // The word obtained by combining the last word of the line and the beginning of the next line 
            // was found in the dictionary: it's probably a full word indeed
            output += line.substring(0,j+1)+"<span class=\"replaced\">"+lastWord+"</span>";
         } else {
            // The word starting in the end of the line and ending on the beginning of the next line is probably a compound word with a -
            output += line.substring(0,j+1)+"<span class=\"candidate\">"+lastWord+"</span>-";
         }
         // Move to the end of this line the end of the (simple or compound) word previously in the beginning of the next line
         if(i<textTable.length-1){
            var nextLineParts = splitNextLine(textTable[i+1]);
            output += nextLineParts[0]+"<br/>";
            textTable[i+1] = nextLineParts[1]
         }
      } else {
         output += line+"<br/>";
      }
      i+=1;
   }

   // Add the last treated line to the output
   output += textTable[textTable.length-1];
   return output;
}