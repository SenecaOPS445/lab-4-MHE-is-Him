#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):
    return s[:5]  # Get the first 5 characters

def last_seven(s):
    return s[-7:]  # Get the last 7 characters

def middle_number(n):
    num_str = str(n)  # Convert number to string
    return num_str[1:3]  # Extract the second and third characters

def first_three_last_three(s1, s2):
    return s1[:3] + s2[-3:]  # First 3 of s1 + Last 3 of s2

if __name__ == '__main__':
    print(first_five(str1))  # Output: Hello
    print(first_five(str2))  # Output: Senec
    print(last_seven(str1))  # Output: World!!
    print(last_seven(str2))  # Output: College
    print(middle_number(num1))  # Output: 50
    print(middle_number(num2))  # Output: .5
    print(first_three_last_three(str1, str2))  # Output: Helege
    print(first_three_last_three(str2, str1))  # Output: Send!!
