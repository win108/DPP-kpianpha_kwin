#!/usr/bin/env python3

a=int(input("Enter a number less than 25\n"))

if a>25 :print("Error")
else : 
    for i in range(25-a+1):
        print("Inside the loop, my variable is",a+i)