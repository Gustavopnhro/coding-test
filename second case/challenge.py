#input: "Hello, World"
#output: "Helo, Wrd!"

phrase = "Hello, World!"
splitedPhrase = []
newPhrase = []
for letter in phrase:
    splitedPhrase.append(letter)

for i in range (0, len(splitedPhrase)):
    if splitedPhrase[i] not in newPhrase :
        newPhrase.append(splitedPhrase[i])
    
print(newPhrase)