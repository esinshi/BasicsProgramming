'''
Basics of Programming
04 September 2023

Exercise 2:

Write a function that can:
List letters a,b,c
List integers 1,2,3

'''

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]


def func1(list_letter, list_number):
    newList = []
    for i in range(len(list_letter)):
        newList.append(list_letter[i])
        newList.append(list_number[i])
    return newList


print(func1(letters, numbers))
