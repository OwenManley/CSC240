# -*- coding: utf-8 -*-
"""
Owen Manley, CSC 240, Assignment #5.
- This assignment prompts the user to enterthe height for a pascal triangle.
The user will also have the ability to exitor terminate the program every time
a triangle is generated.
"""
def main():
    """Main method for running the program. First while loop is for user prompt in
asking whether or not they want to continue. Second one is for error handling.
Was wanting to do more but  I got lazy."""
    cont = True
    while cont:
        print("\t- Pascal's Triangle Generator -\n\n")
        while True:
            try:
                height = int(input("Please enter the height of your desired pascal's triangle: "))
                if height < 1:
                    print("Integer must be positive.")
                    continue
                else:
                    break
            except ValueError:
                print("Input must be an integer.")
        triangle = generate(height)
        print("\t- Generated Triangle -\n\n")
        print_triangle(triangle)
        looper = input("Would you like to produce another one of Pascal's Triangles? '1' - Yes or '2' - No: ")
        if looper == '2':
            print("Thanks for stopping by!")
            cont = False
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def make_new_row(old_row):
   
    """Requires:
       -- list old_row that begins and ends with a 1 and has zero or more
          integers in between (has to have at least [1,1])
       Returns:
       -- list beginning and ending with a 1 and each interior (non 1)
          integer is the sum of the corresponding old_row elements
          For example if old_row = [ 1,4,6,4,1], then new_row = [1,5,10,10,5,1],
          i.e. 5=1+4, 10=4+6, 10=6+4, 5=4+1 """
    if not old_row:
        return [1] #For handling the first row. First row will be [1].
    elif old_row == [1]:
        return [1,1] #For handling second row. If the one before it is [1], return [1,1].
    new_row = [1] #After the first 2 rows, input a '1' on the leftmost side after every row.
    for i in range(len(old_row) - 1): #Used for iterating through the rows and adding the values. 
        new_row.append(old_row[i] + old_row[i + 1])
    new_row.append(1) #Adding '1' on the rightmost side after every row. 
    return new_row
#-----------------------------------------------------------------------------------------------------------------------------------------------------------   
def generate(height): #Generation of the triangle.
    triangle = [] #Empty list first.
    if height >= 1:#If the height is > 1, generate the first row.
        triangle.append([1])
    for i in range(1, height):
        triangle.append(make_new_row(triangle[-1] if triangle else [1]))
        #After that, generate the next row and add it to the list for it to grow. ^
    return triangle #Return the generated triangle.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def print_triangle(triangle):
    width = len(str(triangle[-1][len(triangle[-1]) // 2]))
#^ Calculates the width of the widest number to ensure there is space to align.
    for i, row in enumerate(triangle):
#^ Iterates over the list where 'i' is the index, and row is the row itself.
        spacing = " " * ((width - 1) * (len(triangle) - len(row)))
#^Calculates spacing for aligning the center.
        format_row = [str(j).center(width) for j in row]
#^Creates a new list where each element of the row is centered within 'width'.
        print(spacing + " ".join(format_row))
#^Prints the row, printing the spacing then joins the elements 'format_row' with a space in between.
#Resulting in the complete triangle.        