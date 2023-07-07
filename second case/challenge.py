#input: "Hello, World"
#output: "Helo, Wrd!"

phrase = "Hello, World!"
splitedPhrase = []
newPhrase = []
for letter in phrase:
    if letter not in newPhrase:
        newPhrase.append(letter)

print(''.join(newPhrase))
