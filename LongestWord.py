'''Implement a function longestWord() that takes a list of words and returns the longest
one.'''

#Define the function with parameter 'wordList' as a list of words
def longestWord(wordList):
    
    #variable to store longest word
    longestWord=wordList[1]
    
    #loop the list to find the largest word
    for x in wordList:
        
        #check if current words length is greater than max word length
        if len(x)>len(longestWord):
            
            #assign the new longest word
            longestWord=x
            
    #return the longest word
    return longestWord
    
#Define list of words
wordList = ["BarryAllen", "BruceWayne", "ElenaGilbert", "ClarkKent", "EmiliaClark"]

#Call the function and print the output
print("The Longest word in the List is : "+longestWord(wordList))