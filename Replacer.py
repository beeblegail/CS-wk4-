#Author: NMB
#Date: 31/01/2018
#Title: ************
#Version: 1.0

word = ''

while word != 'x':
    word = input("Please enter a word: ")

    # store the characters of the word in a list
    letters = list(word)

    length = len(word)

    for i in range(0, int(length)):
        if( letters[i] == 'a' or letters[i] == 'A' ):
            letters[i] = '4'
        elif( letters[i] == 'e' or letters[i] == 'E' ):
            letters[i] = '3'
        elif( letters[i] == 'i' or letters[i] == 'I' ):
            letters[i] = '1'
        elif( letters[i] == 'o' or letters[i] == 'O' ):
            letters[i] = '0'
        elif( letters[i] == 'u' or letters[i] == 'U' ):
            letters[i] = '|_|'

    # join all the letters together to make a new word
    new_word = "".join(letters)
       
    print(new_word)
    
    print('==============================')  

