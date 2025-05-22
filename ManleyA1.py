# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 21:43:04 2024

Owen Manley
Assignment #1
This assignment puts user-inputted floating point
numbers into increasing order.
"""
#-------------------------------------------------------------------------------------------------------------
#A while loop used later.
cont = True
while cont: 
    print("--- NUMBER ORGANIZER ---\n\n")

    first_number = float(input("Enter first floating-point number:\n"))
    second_number = float(input("Enter second floating-point number:\n"))
    third_number = float(input("Enter third floating-point number:\n"))
#-------------------------------------------------------------------------------------------------------------
#MEATOFCODE
#While loop for dealing with duplicates.
    while first_number == second_number or first_number == third_number or second_number == third_number:
        print("Duplicate(s) not allowed. Try again!\n\n")
    
        first_number = float(input("Enter first floating-point number:\n"))
        second_number = float(input("Enter second floating-point number:\n"))
        third_number = float(input("Enter third floating-point number:\n"))
#If statements for moving the three numbers into increasing order.
#Couldn't figure out how to make the spaces between the printed commas go away.    
    if first_number < second_number < third_number:
        print("Numbers in increasing order: ",  first_number,",",second_number,",",third_number)
    elif first_number < third_number < second_number:
        print("Numbers in increasing order: ",  first_number,  ",", third_number,  ",",  second_number,"\n\n")
    elif second_number < first_number < third_number:
        print("Numbers in increasing order: ",  second_number,  ",", first_number,  ",",  third_number,"\n\n")
    elif second_number < third_number < first_number:
        print("Numbers in increasing order: ",  second_number,  ",", third_number,  ",",  first_number,"\n\n")
    elif third_number < second_number < first_number:
        print("Numbers in increasing order: ",  third_number,  ",", second_number,  ",",  first_number,"\n\n")
    else:
        print("Numbers in increasing order: ",  third_number,  ",", first_number,  ",",  second_number,"\n\n")
#-------------------------------------------------------------------------------------------------------------
#The while loop at the beginning of the program was for whether or not the user wanted
#to add another set of numbers. If not, the program terminates with a nice goodbye message.
    looper = input("Would you like to enter different numbers? (Enter Y or N non-case sensitive):")
    if looper.lower() == 'n':
        print("Goodbye!")
        cont = False
        
        
    
    
    