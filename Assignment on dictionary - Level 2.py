'''
Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers. 
Assume that the words contain only uppercase letters and the maximum word length is 10.
'''
#lex_auth_01269444890062848087

def find_correct(word_dict):
    #start writing your code here
    result = []
    correct,almost,wrong = 0,0,0
    
    for key,value in word_dict.items():
        if(key==value):
            correct+=1 
        elif(len(key)!= len(value)):
            wrong +=1 
        else:
            word1 = key 
            word2 = value
            count = 0 
            index = 0
            
            for i in word1:
                j = word2[index]
                if(i!=j):
                    count += 1
                    index += 1
                else:
                    index += 1
                    
                    
            
            if(count<3):
                almost += 1
            else:
                wrong += 1
                
    
    result = result + [correct] + [almost] + [wrong]
    return result

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
