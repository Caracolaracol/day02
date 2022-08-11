# ----DATA TYPES----

#strings
print("Hello"[0]) # H
print("Hello"[4]) # o
print("134" + "345") # Here we get: 134345 # as a string, concatenated both strings

#Integer: numeros enteros, osea si decimal
print(123 + 345) # 468 

#Boolean
True
False


# Type error, type checking, type conversion
num_char = len/input("What is your name?")
print(type(num_char)) # console says int # data type is int

new_num_char = str(num_char) #str convert into a string
print("Your name has " + new_num_char + " characters.") # console: your name has 6 characters.

a = str(123)
print(type(a)) # console: data type: str
b = float(123)
print(type(a)) # console: float

# exercise

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(int(two_digit_number[0]) + int(two_digit_number[1]))

#Mathematical operations

#RULE: PEMDAS, left to right
#niveles de prioridad en la operacion matemática
# ()
# **
# * /
# + -

3 * 3 + 3 / 3 - 3 # si ejecutara esto daría: 7

# BMI Calc

height = input("Enter your height in m: ")
weight = input("enter your weight in kg: ")
weight_as_int = int(weight)
height_as_float = float(height)

#ways to calculate bmi:
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEDMAS
bmi = weight_as_int / (height_as_float * height_as_float)
bmi_as_int = int(bmi)
print(bmi_as_int)
