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


# store in the folder variable the address of the folder containing this program
folder = os.path.abspath(os.path.dirname(sys.argv[0]))

# Load the DELAF transformed into UTF-8 (http://infolingu.univ-mlv.fr/DonneesLinguistiques/Dictionnaires/telechargement.html)
# DELAF is available under the LGPLLR license (http://infolingu.univ-mlv.fr/DonneesLinguistiques/Lexiques-Grammaires/lgpllr.html)
input = open(os.path.join(folder,"dela-fr-public-utf8.dic"),"r",encoding="utf-8")
delafWordsWithANonFinalS = {}
delafWordsWithAnF = {}

for line in input:
  # keep only the word (before the first comma)
  res = re.search("^([^,]+),.*$",line)
  if res:
     word = res.group(1)
     # Check if the word contains an s (except in last position)
     # that is it may contain a « long s » instead of an f
     res = re.search("^[^ ]*s[^ ]+$",word)
     if res:
        delafWordsWithANonFinalS[word] = 1
     # Check if the word contains an f
     res = re.search("^[^ ]*f[^ ]*$",word)
     if res:
        delafWordsWithAnF[word] = 1

print(str(len(delafWordsWithANonFinalS))+" words containing at least one non final s were found")
print(str(len(delafWordsWithAnF))+" words containing at least one f were found")

maxNbOfS = 0
sWord = ""
possibleMistakes = {}
ambiguities = {}
i = 0
for word in delafWordsWithANonFinalS:
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
      if variant in delafWordsWithAnF:
         # here there is an ambiguity with a word containing an f!
         possibleMistakes[variant].append(variant)
      if len(possibleMistakes[variant])>1:
         # if an ambiguity was found, save it to ambiguities
         if not(str(possibleMistakes[variant]) in ambiguities):
            ambiguities[str(possibleMistakes[variant])] = 1

# save a dictionary of possible corrections
output = open(os.path.join(folder,"fs-resources.js"),"w",encoding="utf-8")
output.writelines("""// liste des mots ci-dessous provenant du dictionnaire DELAF (http://infolingu.univ-mlv.fr/DonneesLinguistiques/Dictionnaires/telechargement.html)
// disponible sous licence LGPLLR (http://infolingu.univ-mlv.fr/DonneesLinguistiques/Lexiques-Grammaires/lgpllr.html)
// traité par le script build-fs-resources.py

var dictionary = {
""")

for variant in possibleMistakes:
   output.writelines('"'+variant+'":'+str(possibleMistakes[variant]).replace(", ",",")+',\n')

output.writelines("}")
output.close()
"""
# print ambiguities: saved in ambiguites-f-s_longs.txt
for ambiguity in ambiguities:
   print(ambiguity)
"""

input.close()