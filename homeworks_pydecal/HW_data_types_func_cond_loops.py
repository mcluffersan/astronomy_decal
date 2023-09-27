
#Homework 3: Data Types, Functions, Conditionals, and Loops



""" ### Problem 1: Power of a Number:
Write a function to compute the value of x raised to the power y (x^y) 
without using the built-in pow or ** operator.
"""

def power(input, power): #this is considering if they already have input and power
   x = 1 # counter
   q = input #so it doesnt multiply by itself
   while power > x: #looop
      input = input * q
      x += 1
      print(input)



"""### Problem 2: Minimum and Maximum
Write a function that takes a list of numbers as input and returns the 
minimum and maximum values in the list as a tuple.
"""

def minandmax(list1):
   max1 = (max(list1))
   min1 = (min(list1))
   test = []
   test.append(min1)
   test.append(max1)
   test = tuple(test)
   print(test)
   print(type(test))

"""### Problem 3: Check Leap Year
Write a function that takes a year as input and returns True if it's a 
leap year, and False otherwise. A leap year is divisible by 4 but not divisible 
by 100 unless it is also divisible by 400.
"""

def leapYear(year):
  year = int(input("what year to do you want"))
  if year%4 != 0: #If 4 is not divisible by 0 x = false, opposite if true
     x = False
  else:
     x = True
  print(x)



"""### Problem 4: Calculate BMI (Body Mass Index):
Write a function that takes a person's weight (in kilograms) and height 
(in meters) as input and returns their BMI.
"""

def calculate_bmi(weight, height):
   weight = int(input("what is your weight"))
   height = int(input("whats your height"))
   bmi = (weight/height**2)
   print(bmi)
   return bmi



"""### Problem 5: Rotating Digits
Implement a function called rotate_digits that takes an integer n as input and 
rotates its digits to the right by one position. For example, given the input 12345, 
the function should return 51234. You may *not* convert the input to a string but 
you can use properties of a string in your answer.

**Hint:** Use modulus (%) and floor division (//). For example, 12345 % 10 = 5 and 
12345 // 10 = 1234
"""

def rotate_digits(digits):
   x = int(input("Put a Number Here:")) #input
   y = x #important to keep the x originally the same number
   digits = 0

   while x > 0: #counts the amount of digits
      digits += 1
      x //= 10 #modular division to see how many times it could be divided by 10

   x = y # reverts x back to how it was

   leftdigit = x // pow(10,digits - 1) #x is dividing by 10 to the power of digits - 1 so you can record left digit

   x = x % (leftdigit * 10**(digits-1)) #finding the remainder if you get rid of left number

   x = (x*10) + leftdigit #adding left number to the right
   print (x)





### For questions #6-10, write the solution with a for-loop and a while-loop.
# If it is not possible to write it with a for-loop or while-loop, detail why.

"""Problem 6: Maximum
Given a list of numbers, find the maximum number. Use a for-loop and a while-loop.
"""

list1 = [1, 3, 5, 7, 4, 6]

def findMax(lis):
   list1 = [1, 3, 5, 7, 4, 6]
   y = 0 #assuming if you dont have any numbers under 0
   for i in list1:
      
      x = i
      if y < x:
         y = x
      else:
         pass
   print(y)




"""Problem 7: Minimum
Given a list of numbers, find the minimum number. Use a for-loop and a while-loop.
"""

list1 = [1, 3, 5, 7, 4, 6]

def findMin(lis):
   list1 = [1, 3, 5, 7, 4, 6]
   y = list1[2] #if you have one number in the list you can probbaly use this
   for i in list1:
      
      x = i
      if y > x:
         y = x
      else:
         pass
   print(y)

"""Problem 8: The Product
Given a list of numbers, calculate the product of all the numbers.
"""

def product(numList):
   numlist = [1, 3, 5, 7, 4, 6]
   x = 1 #have to define x
   for i in numlist:
       x *= i

   print(x)

"""Problem 9: Vowels
Given a string, count the number of vowels in it using a for loop.

"""

string1 = "pneumonoultramicroscopicsilicovolcanoconiosis"

def countVowels(str):
   string1 = "pneumonoultramicroscopicsilicovolcanoconiosis" #string
   counter = 0 #counter for how many vowels
   for i in string1:
      if i == "i": #i know there was a way to do it in one if statement using or, wasn't 100% how to do it though
         counter += 1
      elif i == "a":
         counter += 1
      elif i == "o":
         counter += 1
      elif i == "u":
         counter += 1
      elif i == "e":
         counter += 1
      else:
         pass
   print(counter)



"""Problem 10: Sum of Digits (Digital Root):
Given an integer, return the sum of its digits (also known as the digital 
root) For example, if the input is 12345, the output should be 15 
(1 + 2 + 3 + 4 + 5).

**Hint:** Refer to #5!

"""

# For this question, it is harder to do it as a for-loop as there is no 
# way of keeping track of all the digits.
# So, only a while-loop solution is necessary.

def sumDigits(num):
   x = int(input("Put a Number Here: ")) #input
   y = x #keeps x number
   digits = 0 

   while x > 0: #used to count number of digits in number
      digits += 1
      x //= 10

   finalnum = 0 #will be used to find the total sum of number

   while digits > 0: #function used to add up sum
      leftdigit = y // pow(10,digits - 1) #Isolate digits

      y = y % (leftdigit * 10**(digits-1))#Finds remainder and reassigns y
      
      finalnum = finalnum + leftdigit#Adds Sum
      
      digits -= 1
   print(finalnum)
