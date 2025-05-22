# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 23:27:13 2024

Owen Manley, CSC 240, Assignment #2. This assignment has a user enter specified 
dimensions and gives information regarding those corresponding dimensions for
a flowerbed.

I'm not entirely sure if the sample run for this assignment is accurate. I kept
getting the same results for the output when using the input values in the 
sample run. I did multiple iterations to configure my program to see if it 
would change the results, but it did not.
"""
#Importing math allows the ability to find the radius and area
#of the flowerbeds by using pi. Has additional funcionalities as well.
import math
cont = True

print("""\t-Calculating Garden Requirements-
 \t---------------------------------\n""")
while cont:
    side_length = float(input("Enter length of side of garden (in feet): "))
    spacing = float(input("Enter spacing between plants (in feet): "))
    flowerbed_depth = float(input("Enter depth of garden soil (in feet): "))
    fill_depth = float(input("Enter depth of fill (in feet): "))
    print("")
#------------------------------------------------------------------------------
#Area calculations
    radius = side_length/2
    circle_area = math.pi * (radius **2)
    semicircle_area = circle_area/2
#------------------------------------------------------------------------------
#Calculations for number of plants
    plants_per_square_foot = 1/(spacing **2)
    plants_per_flowerbed = int(circle_area * plants_per_square_foot)
    plants_per_semiflowerbed = int(semicircle_area * plants_per_square_foot)
    total_plants = plants_per_flowerbed + 2 * plants_per_semiflowerbed
#------------------------------------------------------------------------------
#Calculations for soil
#Dividing by 27 is used to calculate cubic yards.
    flowerbed_soil = circle_area * flowerbed_depth/27
    semiflowerbed_soil = semicircle_area * flowerbed_depth/27
    total_soil = (flowerbed_soil + 2 * semiflowerbed_soil)
#------------------------------------------------------------------------------
#Calculation for fill 
    total_fill = ((circle_area + 2 * semicircle_area) * fill_depth)/27
#------------------------------------------------------------------------------
#Display for results
#The round function is used to round a number to the desired decimal places to 
#the right. In this case, just one.
    print(""" \t---------------------------------\n
      \t\t -Requirements-\n""")
    print("Plants for each semicircle garden: ", plants_per_semiflowerbed)
    print("Plants for the circle garden: ", plants_per_flowerbed)
    print("Total plants for garden: ", total_plants)
    print("Soil for each semicircle garden: ", round(semiflowerbed_soil, 1), "cubic yards.")
    print("Soil for the circle garden: ", round(flowerbed_soil, 1), "cubic yards.")
    print("Total soil for the garden: ", round(total_soil, 1), "cubic yards.")
    print("Total fill for the garden: ", round(total_fill, 1), "cubic yards.")
    print("")
#while loop for whether or not user would like to continue.
    looper = input("""Would you like to calculate a different flower garden? ('1' for yes '2'-- 
for termination): """)
    print("")
    if looper == '2':
        print("Goodbye!")
        cont = False

