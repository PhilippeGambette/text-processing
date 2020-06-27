#!/usr/sfw/bin/python
# -*- coding: utf-8 -*-

import glob, os, re, sys, requests
from xml.dom import minidom
import csv


# get all possible variants obtained by replacing any s with an f or keeping it
def fVariants(word):
   fWords = [""]
   i = 0
   # For each letter, check if it is an s
   while i < len(word):
      if (word[i]!="s") or (i == len(word)-1):
         # The letter is not an s or it is the final s of a word, 
         # just add it to all variants
         j = 0
         while j < len(fWords):
            fWords[j] += word[i]
            j += 1
      else:         
         # The letter is an s which is not the final letter of the word:
         # add an f to all variants
         # and also add an s to all variants
         oldFWordNb = len(fWords)
         j = 0
         while j < oldFWordNb:
            fWords.append(fWords[j]+"f")
            fWords[j] += "s"
            j += 1
      i += 1
   #print(str(fWords[1:len(fWords)]))
   return fWords[1:len(fWords)]


# load a dictionary where each line starts with a word
# (considered a sequence of characters non containing a comma or a space or a tabulation)
# before a special separator character (e.g. comma for DELAF, tab for Lexique, etc.)
# and update a dictionary wordsWithANonFinalS of all words containing a non final s 
# and a dictionary wordsWithAnF of all words containing an f
def loadWords(input, separator, wordsWithANonFinalS, wordsWithAnF):
  for line in input:
    # keep only the word (before the first occurrence of a separator)
    res = re.search("^([^"+separator+"]+)"+separator+".*$",line)
    if res:
      # remove any \ from the word (present in DELAF)
      word = res.group(1).replace("\\","")
      # Check if the word contains an s (except in last position)
      # that is it may contain a « long s » instead of an f
      res = re.search("^[^ 	,]*s[^ 	,]+$",word)
      if res:
        wordsWithANonFinalS[word] = 1
      # Check if the word contains an f
      res = re.search("^[^ 	,]*f[^ 	,]*$",word)
      if res:
        wordsWithAnF[word] = 1
  print("A total of "+str(len(wordsWithANonFinalS))+" words containing at least one non final s were found")
  print("A total of "+str(len(wordsWithAnF))+" words containing at least one f were found")


##############################################
# LOAD LINGUISTIC RESOURCES
##############################################
# store in the folder variable the address of the folder containing this program
folder = os.path.abspath(os.path.dirname(sys.argv[0]))
wordsWithANonFinalS = {}
wordsWithAnF = {}
# the suffix "nc" will be added to output file names if the script
# uses resources which may not be used for commercial purposes.
suffix = ""

# Load the DELAF transformed into UTF-8 (http://infolingu.univ-mlv.fr/DonneesLinguistiques/Dictionnaires/telechargement.html)
# DELAF is available under the LGPLLR license (http://infolingu.univ-mlv.fr/DonneesLinguistiques/Lexiques-Grammaires/lgpllr.html)
print(" ")
print("Loading the DELAF")
input = open(os.path.join(folder,"dela-fr-public-utf8.dic"),"r",encoding="utf-8")
loadWords(input,",",wordsWithANonFinalS,wordsWithAnF)
input.close()

# Load the Lexique 3.83 database (http://www.lexique.org)
# Lexique is available under the CC BY SA 4.0 license (https://creativecommons.org/licenses/by-sa/4.0)
print(" ")
print("Loading the Lexique database")
input = open(os.path.join(folder,"Lexique383.tsv"),"r",encoding="utf-8")
loadWords(input,"	",wordsWithANonFinalS,wordsWithAnF)
input.close()

"""
# Load a list of words containing an s built by Simon Gabay from LGeRM (http://www.atilf.fr/LGeRM)
# LGeRM is available under the CC BY NC SA 3.0 license (https://creativecommons.org/licenses/by-nc-sa/3.0/fr/)
suffix = "-nc"
print(" ")
print("Loading part of the LGeRM database")
input = open(os.path.join(folder,"LGeRM-s.txt"),"r",encoding="utf-8")
loadWords(input,"	",wordsWithANonFinalS,wordsWithAnF)
input.close()
"""

##############################################
# COMPUTE POSSIBLE MISTAKES AND AMBIGUITIES
##############################################
maxNbOfS = 0
sWord = ""
possibleMistakes = {}
ambiguities = {}
i = 0
print("")
print("Building the list of words for the fs script and the list of ambiguities")
for word in wordsWithANonFinalS:
   # compute number of s in the word
   #numberOfS = len(word)-len(word.replace("s",""))
   #print(str(fVariants(sWord)))

   # add to possibleMistakes all possible variants replacing s with f
   for variant in fVariants(word):
      if variant in possibleMistakes:
         # here there is an ambiguity between two possible explanations of the variant!
         possibleMistakes[variant].append(word)
         #print(variant+" : "+str(possibleMistakes[variant]))
      else:
         possibleMistakes[variant] = [word]
      if variant in wordsWithAnF:
         # here there is an ambiguity with a word containing an f!
         possibleMistakes[variant].append(variant)
      if len(possibleMistakes[variant])>1:
         # if an ambiguity was found, save it to ambiguities
         if not(str(possibleMistakes[variant]) in ambiguities):
            ambiguities[str(possibleMistakes[variant])] = 1


##############################################
# OUTPUT JAVASCRIPT RESOURCE FILE
##############################################
# save a dictionary of possible corrections
output = open(os.path.join(folder,"fs-resources"+suffix+".js"),"w",encoding="utf-8")
output.writelines("""// The list of words below was obtained by the script build-fs-resources.py
// available at https://github.com/PhilippeGambette/text-processing/tree/master/fs, using data:
// from DELAF (http://infolingu.univ-mlv.fr/DonneesLinguistiques/Dictionnaires/telechargement.html)
// available under the LGPLLR license (http://infolingu.univ-mlv.fr/DonneesLinguistiques/Lexiques-Grammaires/lgpllr.html)
// from Lexique 3.83 (http://www.lexique.org)
// available under the CC BY SA 4.0 license (https://creativecommons.org/licenses/by-sa/4.0)""")
if suffix == "-nc":
   output.writelines("""
   // from a list of words containing an s built by Simon Gabay from LGeRM (http://www.atilf.fr/LGeRM)
   // available under the CC BY NC SA 3.0 license (https://creativecommons.org/licenses/by-nc-sa/3.0/fr/)""")

output.writelines("""
var dictionary = {
""")

for variant in possibleMistakes:
   output.writelines('"'+variant+'":'+str(possibleMistakes[variant]).replace(", ",",")+',\n')

output.writelines("}")
output.close()


##############################################
# OUTPUT AMBIGUITIES
##############################################
output = open(os.path.join(folder,"ambiguites-f-s_longs"+suffix+".txt"),"w",encoding="utf-8")
print(" ")
print("Listing ambiguities...")

for ambiguity in ambiguities:
   print(ambiguity)
   output.writelines(str(ambiguity)+"\n")
output.close()