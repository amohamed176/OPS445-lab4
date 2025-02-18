#!/usr/bin/env python3

# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(input_str):
    # Returns the first five characters of the input string
    return input_str[:5]

def last_seven(input_str):
    # Returns the last seven characters of the input string
    return input_str[-7:]

def middle_number(input_num):
    # Converts the number to string and returns the second and third characters
    num_str = str(input_num)
    if len(num_str) > 2:
        return num_str[1:3]
    return num_str

def first_three_last_three(input_str1, input_str2):
    # Returns a string combining the first three characters of input_str1 and the last three characters of input_str2
    return input_str1[:3] + input_str2[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
