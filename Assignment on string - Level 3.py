"""
Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence. 

Rules are as follows: 
a. Spaces are to be retained as is 
b. Each word should be encoded separately

If a word has only vowels then retain the word as is

If a word has a consonant (at least 1) then retain only those consonants

Note: Assume that the sentence would begin with a word and there will be only a single space between the words.
"""
#lex_auth_01269444961482342489

def sms_encoding(data):
    #start writing your code here
    words = data.split()
    vov = "aeiouAEIOU"
    result = ""
    
    for i in words:
        if(len(i)==1):
            result += i 
            
        
        else:
            for letter in i:
                if letter not in vov:
                    result += letter
                
        
        result += " "
    
    
    return result[0:-1]

data="I love Python"
print(sms_encoding(data))
