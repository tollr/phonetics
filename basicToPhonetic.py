myDict = {
  "j": "ʒ",
  "eu": "ø",
  "ai": "ɛ",
  "è": "ɛ"
}

sentence = "je suis jar-jar binks"

# 0 -> key : j
# 0 -> myDict[j] : ʒ
# for key in myDict:
# print(key + " " + myDict[key])

result = ""
for letter in sentence:
  if letter in myDict:
    result += myDict[letter]
  else:
    result += letter

print(result)
