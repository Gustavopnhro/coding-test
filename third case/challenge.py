#input: "babad"
#output: "bab"

phrase = "babad"
splitedPhrase = []
palindrome = []

for letter in phrase:
    splitedPhrase.append(letter)


for i in range(0, len(splitedPhrase)):
    palindrome.append(splitedPhrase[i])
    print('Phrase = '+ phrase[0:i+1] )
    print ('Palindrome ='+''.join(palindrome))
    if ''.join(palindrome) in phrase[::-1] and len(palindrome)>2:
        break

    

print(palindrome)