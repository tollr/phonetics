# -*- coding: utf-8 -*-
# import de la bibliothèque python regular expression
import re

# dictionnaire
myDict = {
  "j": "ʒ",
  "eu": "ø",
  "ai": "ɛ",
  "è": "ɛ"
}

# fonction
def letterToSound(sentence, target):
  regex = re.compile(target)
  searchResults = []

  # recupération des index ou se trouvent la target
  for match in regex.finditer(sentence):
    searchResults.append(match.start())

  # string to list pour modifier un index (hack...)
  sentenceArray = list(sentence)

  # boucle sur les index d'apparition de l'expression et remplacement
  # par la correspondance dans le dictionnaire myDict[j] -> ʒ
  for i in searchResults:
    sentenceArray[i] = myDict[target]

  # list to string
  endResult = "".join(sentenceArray)

  return endResult

def main(userInput):
  # variable qui est set à chaque tour de boucle
  finalResult = userInput
  
  for i in myDict:
    # variable temporaire pour récupère le résultat d'un tour
    tmpResult = letterToSound(finalResult, i)
    finalResult = tmpResult
  
  return finalResult

# init du programme
print(main("j'aime le jeu de guitare d'henri dès"))
