#input = "hello. how are you? i'm fine, thank you"
#output = "Hello. How are you? I'm fine, thank you."



phrase = "hello. how are you? i'm fine, thank you.".capitalize()

char = ['?', '.', '!']

while True:
    words = phrase.split(' ')
    for i, word in enumerate(words):
        if word[::-1][0] in char and i < len(words)-1:
            words[i+1] = words[i+1].capitalize()
    
    print(' '.join(words))
    phrase = input(str("Insert your phrase: \n")).capitalize()
