#input: "Hello, World! OpenAI is amazing"
#output: ".amazing is OpenAI World! Hello"

phrase = "Hello, World! OpenAI is amazing"
while True:
    splitPhrase = phrase.split(' ')
    splitPhrase.reverse()
    print(' '.join(splitPhrase))
    phrase = input(str("Insert your phrase \n"))
