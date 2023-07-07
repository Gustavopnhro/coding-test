#input = "hello. how are you? i'm fine, thank you"
#output = "Hello. How are you? I'm fine, thank you."



phrase = "hello. how are you? i'm fine, thank you."
words = phrase.split(' ')

for i, word in enumerate(words):
    if words[i][::-1][0] in ['.', '?', '!']:
        print('achei')


print (words[0][::-1][0])