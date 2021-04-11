import string

def reverse(word): 
    reve = "" 
    for i in word: 
        reve = i + reve
    return reve 

def palindrome(reve,word):
    if (reve == word):
        return("Yes")
    else:
        return("Not")
    


word = input('Input Word : ')

prepareWord = set(word)
specialChar = set(string.punctuation)

if (' ' in word or prepareWord.intersection(specialChar)):
    print('Cannot using space and special characters !')
else:
    reversedata = reverse(word)
    check = palindrome(reversedata, word)
    print(reversedata)
    print( "-->",word)
    print("'",check,"'","Palindrome ")
