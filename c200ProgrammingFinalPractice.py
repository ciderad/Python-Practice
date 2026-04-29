# C-200 Final Review

'''
Write a function named getLinesFromFile() that takes an integer n as an argument. The function should open and read from a file named testfile.txt, which you may assume is present in the same directory/folder as the Python code. You may assume that testfile.txt contains plain-text ASCII characters, but you should not assume anything about the file's specific contents, number of lines, or total file length. The function should return a list consisting of the first n lines of text that are in the file. If there are fewer than n lines in the file, the function should return all available lines. For this problem, you don't need to worry about handling file-related errors. Your function definition needs to contain an appropriate docstring. Here is a sample function call:
'''

def getLinesFromFile(n):
    lines = []
    
    with open("testfile.txt", "r") as file:
        l

