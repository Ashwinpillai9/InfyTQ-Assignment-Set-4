"""
Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.

Rules:

The word should have the largest frequency.

In case multiple words have the same frequency, then choose the word that has the maximum length.

Assumptions:

The text has no special characters other than space.

The text would begin with a word and there will be only a single space between the words.

Perform case insensitive string comparisons wherever necessary.
"""
#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    word = ""
    frequency = 0
    words = data.lower()
    words = words.split()
    unique = []
    freq = {}
    maxi = []
    
    for i in words:
        if i not in unique:
            unique.append(i)
            
    
    for i in range(0,len(unique)):
        count = words.count(unique[i])
        freq.update({unique[i]:count})
    

    for key,value in freq.items():
        if(frequency< value):
            frequency = value
            word = key
            
    
    for key,value in freq.items():
        if(frequency == value):
            maxi.append(key)
        

    #start writing your code here
    #Populate the variables: word and frequency
    word  = maxi[0]
    
    for i in range(1,len(maxi)):
        if(len(word)<len(maxi[i])):
            word = maxi[i]


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    print(word,frequency)

#Provide different values for data and test your program.
data="Listen to the big clock Tick tock tick"
max_frequency_word_counter(data)
