#input: "babad"
#output: "bab"

phrase = "rack"
splitedPhrase = []
palindrome = []

for letter in phrase:
    splitedPhrase.append(letter)


for i in range(0, len(splitedPhrase)):
    palindrome.append(splitedPhrase[i])
    if ''.join(palindrome) == phrase[0:i+2] and len(palindrome)>2:
        break

    
print(''.join(palindrome))