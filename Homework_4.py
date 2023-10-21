##################################################################################################
##################################################################################################
#Problem 0:
#Complete the following function so that it returns the sum of the elements in the list passed as an argument

def sum_elements(arr):
    result = 0
    result = (sum(arr))
    return result

#print(sum_elements([1,2,3,4]))
#print(sum_elements([0]))
#print(sum_elements([]))
#print(sum_elements([-1, 1]))

##################################################################################################
##################################################################################################
#Problem 1:
#Simple Calculator Function
#Define a function called `simple_calculator` that takes two numbers and an operator ('+', '-', '*', or '/')
#as arguments and returns the result of the operation.

def calculator(a,b,oper):
    if oper == "+" :
        return a + b
    elif oper == "-" :
        return a - b
    elif oper == "*" :
        return a * b
    elif oper == "/" :
        if a > 0 and b > 0:
            return a / b
        else:
            print("Cannot divide by 0")
    else:
          pass

#print(calculator(1,2,"+"))
#print(calculator(6,2,"*"))
#print(calculator(10,2,"/"))
#print(calculator(1,2,"-"))


##################################################################################################
##################################################################################################
#Problem 2: Area of Shapes
#Create a module named `geometry` with functions to calculate the area of common shapes
#like a square, rectangle, triangle, and circle.
#Import this module and use it to calculate the areas of different shapes.
import math
def geometry(a, b, shape, c = '1', r = '1'):
    pi = math.pi
    if shape == "square":
        return a * a
    elif shape == "rectangle":
        return a * b
    elif shape == "triangleP":
        p = (a+b+c)/2
        return ((p*(p-a)*(p-b)*(p-c))**0.5)
    elif shape == "triangle":
        return (a*b) / 2
    elif shape == "circle":
        return  pi * (r**2)
    else:
        print("This is not usefully function")

#print(geometry(2,5,"circle",1,5))



##################################################################################################
##################################################################################################
#Problem 3: Temperature Conversion
#Write a program that converts temperatures between Celsius and Fahrenheit.
#Create two functions, one for each conversion

def temperature_conversition_C(cel_temp):
    return cel_temp * (9 / 5) + 32
def temperature_conversition_F(fahr_temp):
    return (fahr_temp - 32) * (5/9)


#print(temperature_conversition_F(0))
#print(temperature_conversition_C(0))


##################################################################################################
##################################################################################################
#Problem 4: Online Shopping Cart
#Create a Python program that simulates an online shopping cart using a global dictionary variable.
#Every customer has unique id as a key.
#Define functions to add items to the cart, remove items, calculate the total price,
#and display the contents of the cart.
#Allow the user to interact with the cart by adding and removing items.

customers = {"Vladilen Dimitrov": "0381 111 110",
             "Krasimir Georgiev": "0381 111 111",
             "Krasimir Plamenov": "0381 111 112",
             "Mladen Plamenov": "0381 111 113",
             "Mladen Georgiev": "0381 111 114"
             }

bay_box = {"0381 111 110": "item A",
"0381 111 110": "item B","0381 111 111": "item A",
"0381 111 111": "item B","0381 111 111": "item C",
"0381 111 112": "item D"
}


def del_element_in_box(num):
    return bay_box.pop(num)

print(del_element_in_box("0381 111 112"))

def add_element_in_box(lit):
    return bay_box.update(lit)

print(add_element_in_box({"0381 111 113": "item D"}))