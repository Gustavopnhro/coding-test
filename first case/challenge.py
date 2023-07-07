#input: "Hello, World! OpenAI is amazing"
#output: ".amazing is OpenAI World! Hello"

phrase = "Hello, World! OpenAI is amazing"
splitPhrase = phrase.split(' ')
splitPhrase.reverse()

print(' '.join(splitPhrase))
