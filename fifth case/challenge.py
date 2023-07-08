#input: "racecar"
#output: True

word = "racecar"
while True:
    print(word[::-1] == word)
    word  = input(str("Insert your word: \n"))