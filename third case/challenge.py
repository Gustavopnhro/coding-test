#input: "babad"
#output: "bab"

phrase = "auto"
splitedPhrase = []
palindrome = []

for letter in phrase:
    splitedPhrase.append(letter)


# for i in range(0, len(splitedPhrase)):
#     palindrome.append(splitedPhrase[i])
#     print('Phrase = '+ phrase[0:i+1] )
#     print ('Palindrome ='+''.join(palindrome))
#     if ''.join(palindrome) == phrase.__reversed__ and len(palindrome)>2:
#         break

    
splitedPhrase.reverse()

if ('auto' in ''.join(splitedPhrase)):
    print ("achei")