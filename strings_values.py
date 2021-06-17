String=input("Please enter a string: ")     #taking a string as input
def most_frequent(string):                  #defining a function with 'string' as parameter
    alpha=dict()                            #creating a empty dictionary
    for key in string:          
 '''
      checking the condition: 
      if the first letter in input_string is storing first in dictionary
      return to 1 or else return +=1
 '''
        if key not in alpha:              
            alpha[key]=1
        else:
            alpha[key]+=1
    return alpha
print(most_frequent(String))                #passing the input parameter as argument
        
