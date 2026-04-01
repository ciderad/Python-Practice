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

## YOU CAN EXPECT : "age", "year", "colour"

vals = cideras_dict.values() #.values() returns values of dictionary

## YOU CAN EXPECT : 19, 2006, brown

items = cideras_dict.items() #.items() returns items in the dictionary

#basically the dictionary as a whole

#PRACTICE SETS

cids_set = {9, 22, 6, 6} #unique elements only

#Python ignores duplicates in sets, when you print cids_set you'll get 9, 22, 6

print(cids_set)


