#input: "babad"
#output: "bab"

phrase = "babad"

while True:
    splitedPhrase = []
    palindrome = []

    for letter in phrase:
        palindrome.append(letter)
        if ''.join(palindrome) in phrase[::-1] and len(palindrome)>2:
            break    
    print(''.join(palindrome))
    phrase = str(input("Input your word \n"))

