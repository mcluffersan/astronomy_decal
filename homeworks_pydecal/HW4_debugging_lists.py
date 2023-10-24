"""
HW 4: Debugging and Lists

Q1 Debugging

Throughout this homework, whenever you encounter an error, we would like you to 
explain in a comment what it was and how you fixed it. You can write all these errors 
at any place in the file.



Q2 List Slicing and Striding:

Part 1: Create a variable (name it anything you want but make it descriptive!) that 
is assigned to a list with the numbers 0 to 50. You should not have to write each 
number manually.
"""

# Q2 PART 1 CODE HERE
# I orignally put it so the list would equal list1 = [range[0,51]], It did not work :(
list1 = []
for i in range(0,51):
    list1.append(i)


corn = list1



"""
Part 2: Create a function that takes in a list and squares each element in the list.
"""

# Q2 PART 2 CODE HERE

for i in corn:
    i **= 2
    print(i)

"""
Part 3: You are given two lists: listA and listB. listA contains the integers 1 through 
10 while listB contains the integers 20 through 30. Return a single, new list containing
only the odd integers of both lists in sorted order.
"""

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listB = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# Q2 PART 3 CODE HERE
counter = 0
biglist = listA + listB
for i in biglist:
    if i % 2 != 1:
        biglist.pop(counter) #I was using the .remove() function and I thought that one went by index but it actually goes by value, so I switched to .pop() and it fixed the issue
    counter += 1
biglist.sort()
print(biglist)
"""
Q3 2D Lists
Using nested for loops, create and print a 5x5 2D list with the odd numbers from 1 to 25.
"""

# Q3 PART 1 CODE HERE

# Initialize an empty 5x5 2D list
list_2d = []

# Populate the matrix with odd numbers from 1 to 25
num = 1
for i in range(5):
    row = [] #intializes and resets a row
    for j in range(5):
        if num % 2 == 0:
            row.append("") #if its even it becomes blank space
        else:
            row.append(num)#if its odd it gets added
        num += 1

    list_2d.append(row) #you append the end

#print the 2d list
for row in list_2d:
    print(row)


"""
Now with your completed list_2D, replace all multiples of 3 with '?' character and print
the resulting 2D list.
"""

# Q3 PART 2 CODE HERE
#What conditional can you use to check if numbers are multiples?

# Initialize an empty 5x5 2D list
list_2d = []

# Populate the matrix with odd numbers from 1 to 25
num = 1
for i in range(5):
    row = []

    for j in range(5):
        if num % 2 == 0:
            row.append("")
        else:
            if num % 3 == 0: #if its divisible by 3 it gets replaced with a ?
                row.append("?")
            else: #if it isnt, move with accordance
                row.append(num)

        num += 1

    list_2d.append(row)

# Print the 2D list
for row in list_2d:
    print(row)
"""
Q4 More List Practice

Write a function that takes in a list and returns a copy of that list with duplicate 
values removed.
"""

def remove_duplicates(a):
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                #removes the duplicate
                a.pop(j)
                break #break to avoid error

