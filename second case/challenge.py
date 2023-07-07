#input: "Hello, World"
#output: "Helo, Wrd!"

phrase = "Hello, World!"

while True: 
    splitedPhrase = []
    newPhrase = []
    for letter in phrase:
        if letter not in newPhrase:
            newPhrase.append(letter)
    print(''.join(newPhrase))
    phrase = input('Insert your phrase \n')
