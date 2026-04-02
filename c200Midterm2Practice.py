### This is practice for Midterm 2, following these topics:
		
"""
•	Dictionary view objects: dict_keys, dict_values, dict_items (immutable)
	•	Dictionaries: dict (mutable)
	•	Text file objects: TextIOWrapper (mutable)
	•	Sets: set (mutable, less important)


	•	unbounded loops
	•	modulus and modulo operator
	•	eval()
	•	integer division
	•	Lambda functions
	•	recursion
	•	base case
	•	induction
	•	tail recursion
	•	memoization
	•	persistent storage
	•	file object
	•	file
	•	filename
	•	mode (for a file object)
	•	read mode
	•	write mode
  """

#PRACTICE: Dictionaries

cideras_dict = { "age": 19, "month": "september", "colour":"brown", }

keys = cideras_dict.keys() #.keys() returns the keys in a dictionary
print(keys)
print(type(keys)) #its own distinct type 'dict_keys'

## YOU CAN EXPECT : "age", "year", "colour"

vals = cideras_dict.values() #.values() returns values of dictionary
print(vals)
print(type(vals)) #its own distinct type 'dict_values'
## YOU CAN EXPECT : 19, 2006, brown

items = cideras_dict.items() #.items() returns items in the dictionary
print(items)
print(type(items)) #its own distinct type 'dict_items'

#basically the dictionary as a whole

#PRACTICE SETS

cids_set = {9, 22, 6, 6} #unique elements only

#Python ignores duplicates in sets, when you print cids_set you'll get 9, 22, 6

print(cids_set)

#CATEGORY: MATH & LOGIC

#Floor Division/Integer Division
floorDiv = 10//3
print("The floor division of 10//3 is: ", floorDiv)

#Modulus
remainder = 10%3
print("The remainder of 10/3 using MODULUS (%) is: ", remainder)

#Eval(), evaluates argument as code
eval("15+65")
eval("print('hello')")

#Unbounded loop
while True:
    break

#PRACTICE LAMBDA
#regular add function: 
def add (x, y):
    return x + y

print(add(3, 2))

#now using lambda (temporary function for one time use)
add_lambda = lambda x,y: x+y
print(add_lambda(3,2)) 
## PLEASE PUT THIS SYNTAX ON YOUR INDEX CARD

#FILE STUFF

filename = "data.txt"     # Name of file
mode = "r"                # "r" = Read mode, "w" = Write mode

# TextIOWrapper (File Object - Mutable)
with open(filename, mode) as f:
    content = f.read()    # File object 'f' handles the stream