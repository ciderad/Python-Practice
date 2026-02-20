###
# Hello! This is my way of practicing for my C-200 Midterm!
# Below I will categorize the different objectives of this first third of 
# the course and work through examples as well
#
###


#MIDTERM OBJECTIVE: looping through strings
def all_vowels(text):
    """Counts the number of vowels (a, e, i, o, u) in a string. Compares the number of vowels to the number of letters in the word, to determine whether or not the word only contains values
    
    Parameters:
    text (string): the inputted word

    Returns:
    allVowels(boolean): whether or not the inputted word contains all vowels
    
    """
    vowels = "aeiou"
    count = 0
    allVowels = False
    allVowelList = []
    # Iterate through each character in the input string
    for char in text.lower():
        if char in vowels:
            count += 1
    if count == len(text):
        allVowels = True
    return allVowels

#ALL VOWELS FUNCTION TEST CASES
print("The word eau has all vowels: ", all_vowels("eau"))
print("The word adieu has all vowels: ", all_vowels("adieu"))
print("The word air has all vowels: ", all_vowels("air"))
print("The word air has all vowels: ", all_vowels("euoi"))         


#MIDTERM OBJECTIVE: building a string character by character with a loop

createWord = "wholeheartedly"

def buildStringCharByChar(word):
    """Takes a string and loops through it, then populates a new string with the characters from the inputted string.

    Parameters:
    word (string): inputted word/string

    Returns:
    myWord(string): a new populated string that contains the same letters as word
    """
    myWord = ""
    for letter in word:
        myWord+= letter
    return myWord

#CREATEWORD TESTCASES
print("My word is " + buildStringCharByChar(createWord))


#MIDTERM OBJECTIVE: utilizing the range function

def eulerPi(n):
    """Euler's Function (pi^2/6 = (1/1^2) + (1/2^2) + (1/3^2) + ...)
    
    Parameters:
    n (int): The nth value within the function, i.e. the increasing denominator up until the initial denominiator

    Returns:
    value (int): Euler's Function ran with it
    
    """
    value = 0
    for i in range(n, 0, -1):
        value += 1/(n**2)
        n-=1
    
    return value

data = [1, 5, 10]
#TESTCASES FOR EULERPI FUNCTION
for d in [1, 5, 10]:
    print(eulerPi(d))

#MIDTERM PRACTICE PROBLEM: Utilizing the Zip Function

def zipFunc(x, y, n):
    """This function takes a tuple of three values, the first two tuples are transposed through the zip function
    
    Parameters:
    x(tuple): first inputted tuple transposed with zip (swapped w/ y)
    y(tuple): first inputted tuple transposed with zip (swapped w/ z)
    n(tuple): the final tuple to which the two values will be compared to


    Returns:
    tmp (list): a new list that returns whether the created zip coordinates by row are greater than n
    
    """
    tmp = []
    for x, y in zip(x,y):
        if x + y > n:
            tmp.append(1)
        else:
            tmp.append(0)
    return tmp

#TESTCASES FOR ZIPFUNC FUNCTION
data = [((10, 13, 5), (20, 3, -19), 22),((13, 5), (1, 43, 12, 9), 15),((12, 4, 18, 23, 6),(2, 3, 19),9)]

for d in data:
    print(zipFunc(*d))

#MIDTERM OBJECTIVE: Slicing Strings
def midStr(str1, str2, str3):
    """This functions takes three strings, and returns a new string that is a combination of three strings without the first and last letter of each string 
    
    Parameters:
    str1 (string): first inputted string
    str2 (string): second inputted string
    str3 (string): third inputted string
    
    
    Returns:
    finalStr (string):A string combining str1, str2, str3, without the first and last letters
    
    """
    newStr1 = str1[1:(len(str1)-1)]
    newStr2 = str2[1:(len(str2)-1)]
    newStr3 = str3[1:(len(str3)-1)]

    finalStr = newStr1 + newStr2 + newStr3

    return finalStr

#TESTCASES FOR MIDSTR FUNCTION

st1, st2, st3 = "hello", "world", "!"
print("EXAMPLE 1 OF MIDSTR: " + midStr(st1, st2, st3))
w1, w2, w3 = "python", "i", "hop"
print("EXAMPLE 2 OF MIDSTR: " + midStr(w1, w2, w3))

#MIDTERM OBJECTIVE: Looping through lists

def tipCounter(priceList):
    """Takes a list of integers and computes 20% tip for each value
    
    Parameters:

    priceList (list of int/float): a list of prices (of a split check by person's total)

    Returns:

    tipPriceList (list of int/float): a new list of the respective tip prices at 20 and 15%
    
    """
    tipPriceList20 = []
    tipPriceList15 = []
    for i in range(len(priceList)):
        tipPriceList20.append(round(priceList[i]*0.2,2))
        tipPriceList15.append(round(priceList[i]* 0.15,2))
    
    return tipPriceList20, tipPriceList15

#TESTCASES FOR TIPCOUNTER FUNCTION

table1 = [15.97, 8, 20.55, 30.40, 46]
table2 = [63.90, 78.99, 20, 35.95, 32.45, 40.55, 87.85]
print("Your 20 and 15% tip for your table is", tipCounter(table1))
print("Your 20 and 15% tip for your table is", tipCounter(table2))



