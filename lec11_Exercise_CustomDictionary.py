print("Hi, Welcome to my Dictionary")
print("Enter a term to search in the dictionary")

myDictionary = {"set": "Set is a collection of well defined objects",
                "Alliteration": "Alliteration is the repetition of the beginning sounds of neighboring words.",
                "Anaphora": "Anaphora is a technique where several phrases or verses begin with the same word or words",
                "Hyperbole": "Hyperbole uses exaggeration for emphasis or effect"
                }
query = input()

try:
  print(myDictionary[query])
except:
  print("UH, OH : \nI can't find that word in dictionary")
