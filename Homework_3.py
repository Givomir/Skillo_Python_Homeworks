###################################################################################################
###################################################################################################
#problem 1
#Write a program that takes an integer input from the user and checks if it's odd or even. Use an
#if-else statement to print the result.

#numb = input("Imput your number")
#numb = int(numb)
#if (numb//2):
 #   print("Your number is odd")
#else:
 #   print("Your number is even")

###################################################################################################
###################################################################################################
#problem 2
#Write a Python program to find the sum of all even numbers from 1 to 100 using a loop. Make
#use of control flow constructs like the for loop and conditional statements.
#num = 0
#for i in range(0, 101, 2):
   #print(i)
   #num = num + i
#print(f"The answer is {num}")

###################################################################################################
###################################################################################################
#problem 3
#Write a Python script that prompts the user in the console a simple problem ( how much does 5
#+ 17 equal to ) until the user provides a correct answer.

#answear = 0
#right_an = 5 + 17
#print(right_an)
#while answear != 22:
#     answear = int(input("Hello! Can you tell me how is 5 + 17 equal to"))

###################################################################################################
###################################################################################################
#problem 4
#Write a Python script that iterates over the first 1000 numbers and prints "Fizz" if the number is
#divisible by 3, "Buzz" if it's divisible by 5, and "FizzBuzz" if it's divisible by both 3 and 5.
#digit_1000 = 0
#for digit_1000 in range(0, 1001, 1):
 #  if (digit_1000 % 3 == 0) and (digit_1000 % 5 == 0):
 #     print(f"Digit {digit_1000} FizzBuzz")
 #  elif (digit_1000 % 5 == 0):
  #    print(f"Digit {digit_1000} Buzz")
 #  elif ((digit_1000 % 3 == 0) ):
 #     print(f"Digit {digit_1000} Fizz")
 #  else:
  #    pass

###################################################################################################
###################################################################################################
#problem 5
#Design a Python program that simulates a simple guessing game. The program should generate
#a random number between 1 and 100 and ask the user to guess it. Provide hints like "Too high"
#or "Too low" until the user guesses the correct number. Use a while loop for this game.

#import random
#your_int = 0
#digit = 0
#i = 0
#digit = random.randint(1, 100)
#while your_int != digit:
 #   your_int = input("Right your digit between 1 and 100")
 #   your_int = int(your_int)
 #   if your_int > digit:
 #       print("Your digit is too high")
#    elif your_int < digit:
 #       print("Your digit is too small")
#    else:
#        pass
#    i = i + 1
#print(f"You find the right number from {i} tries")

###################################################################################################
###################################################################################################
#problem 6
#Modify problem 2 so that every time the user is prompted the problem is different. Think of a
#way to design that and come up with a proper solution for that.
#Write a Python script that prompts the user in the console a simple problem ( how much does 5
#+ 17 equal to ) until the user provides a correct answer.

#import random
#answear = 0
#digit_a = 0
#digit_b = 0
#i = 5
#while i != 0:
 #   digit_a = random.randint(1, 100)
  #  digit_b = random.randint(1, 100)
   # answear = int(input(f"Hello! Can you tell me how is {digit_a} + {digit_b} equal to."))
    #if answear == digit_a + digit_b:
     #   print("This is the right answer!")
      #  break
    #else:
     #   print("Try one more time.")

###################################################################################################
###################################################################################################
#problem 7
#Write a Python program that takes an integer input from the user and prints the multiplication
#table for that number from 1 to 10 using a for loop.

#num = 0
#num = int(input("Напишете число за да ви покажа таблицата му за умножение"))
#print(f"таблицана на умножение за чиелото {num} е: ")
#for i in range(0, 11, 1):
  # print(f"{num} * {i} = {num * i}")

###################################################################################################
###################################################################################################
#problem 8
#Create a Python program that checks if a given integer is a prime number.
#Use a for loop to iterate through possible divisors and use an if-else statement to determine if it's prime.

#num = int(input("Input the number "))
#if num >1:
 #   for i in range(2, int(num/2)+1):
 #       if (num % i) == 0:
 #           print(num, "is not prime number")

  #      else:
  #          print(num, "is a prime number")

###################################################################################################
###################################################################################################
#problem 9
#Write a program that takes an integer 'n' as input and prints the following pattern using nested for loops:
 #   1
 #   12
 #   123
 #   1234
 #   12345

num = int(input("Input the number "))
for a in range(1, ((num + 1) - 4)):
    for b in range(1, ((num + 1) - 3)):
        for c in range(1, ((num + 1) - 2)):
            for d in range(1, ((num + 1) - 1)):
                for e in range(1, (num + 1)):
                    print(f"""
                        {a},
                        {a}, {b},
                        {a}, {b}, {c},
                        {a}, {b}, {c}, {d},
                        {a}, {b}, {c}, {d}, {e}
                     """)

