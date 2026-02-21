###
# This is from 02-20-26, where I taught some classmates a bit about Python vocabulary and syntax
# All of the following are examples I came up with to help them understand the concepts they struggled with
###

#def keyword [functioname] ():
myWord= "hey" #global variable

def multiply(a,b):
    print(a)
    print(b)
    mult = a*b #local variable
    return mult

def sayWord(word):
    """
    THIS IS DOCSTRING: This function takes a word and tells the user what the word is

    Parameters: 
    word (str): this is the word passed through the function


    Returns:


    
    """
    print("My word is", word)  #side effect
    return word

#TEST CASE

print("RUNNING SAYWORD FUNCTION: ", sayWord(myWord) ) #using global variable as an ARGUMENT in a function test case

#SLICING

def fruitNinja(fruit1, fruit2):
    fruit1 = fruit1[0:(int(len(fruit1)/2))]
    fruit2 = fruit2[0:(int(len(fruit2)/2))]
    return fruit1, fruit2

#TEST CASE
fr1 = "watermelon"
fr2 = "lemon"
print("RUNNING FRUIT NINJA FUNCTION:", fruitNinja(fr1, fr2))