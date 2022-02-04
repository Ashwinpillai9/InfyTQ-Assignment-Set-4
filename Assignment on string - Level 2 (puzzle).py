"""
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: 

Assume that the sentence would begin with a word and there will be only a single space between the words.

Perform case sensitive string operations wherever necessary.
"""
#lex_auth_01269444195664691284

def encrypt_sentence(sentence):
    #start writing your code here
    word_list = sentence.split(" ")
    count = 1
    vowels = ["a","e","i","o","u"]
    temp = ""
    word = ""
    #eht snu sesir ni eht stea
    
    encoded = ""
    
    for word in word_list:
        cons = ""
        vol = ""
        if(count%2==0):
            for i in word:
                if i in vowels:
                    vol += i 
                else:
                    cons += i 
                
                
            word = cons + vol
            encoded += word + " "
            
            
        
        else:
            encoded += word[::-1] + " "
            
        
        count+=1
    encoded = encoded.strip()
    
    return encoded
    
sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
