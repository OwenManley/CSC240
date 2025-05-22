#Final Python Project, CSC 240, Owen Manley. This program reads from a csv file and look for states with the 
#best and worst case for each indicator. Then, create a text file that prints the results. Drew Kroeger assisted me a little bit so some of my code may be similar to his.
#The code can run but it doesn't display any results. I spent HOURS on this and I couldn't figure it out. I'll leave what I had been working on commented. But,
#I didn't have time to continue working on it so I figured that I might as well recieve some credit for this project.
import csv
def make_trim_list(file_obj, column):
    """ This function takes a CVS file and takes one of the columns, trims the information, 
        and inserts it into a list. 
        Requires: opened file, integer.
        returns, a list of all the numbers in the row thats specified by the column."""
    #print("Inside make_trim_list function")    
    csv_reader = csv.reader(file_obj)

    x_list = []
    x_list_fixed = []
    header = " "

    iteration = 0
    for line in csv_reader:
        if iteration == 5:
            header = line[column]
            iteration += 1
        elif iteration > 5:
            x_list.append(line[column])
        else:
            iteration += 1
        for element in x_list:
            element = element.replace("%","")
            element = element.replace("N/A","-1")
            x_list_fixed.append(element)

        return x_list_fixed, header
    #print('HELLO')
def get_maximums_and_states(big_list, state_list):
    """ Takes the max value in a list. 
        Requires: A list of numbers, list of states in alphabetical order.
        Returns: Largest number in the list and the state associated with the max."""
    max_value = float('-inf')  # Initialize to negative infinity
    state = ""
    
    for element in range(0, len(big_list)):
        big_list[element] = float(big_list[element])

    for element in big_list:
        if element > max_value:
            max_value = element

    if max_value == float('-inf'):  # If max_value is still negative infinity, no valid maximum found
        return None, None

    index = big_list.index(max_value)
    state = state_list[index]

    return max_value, state
    """
    maximum = 0
    state = ""
    for element in range(0, len(big_list)):
        big_list[element] = float(big_list[element])
    maximum = 0
    for element in big_list:
        if element > maximum:
            maximum = element
    index = big_list.index(maximum)
    state = state_list[index]
    print("Maximum value:",maximum)
    print("Maximum value state:",state)

    return maximum, state
    """

def get_min_and_states(big_list, state_list):
    """ Takes the min value in a list. 
        Requires: A list of numbers, list of states in alphabetical order.
        Returns: Smallest number in the list and the state associated with the min.
    """
    """
    minimum = 0
    state = ""

    for element in range(0, len(big_list)):
        big_list[element] = float(big_list[element])
    #iteration = 0
    #minimum = 999999
    for element in big_list:
        if element < minimum and element > -1:
            minimum = element

    index = big_list.index(minimum)
    state = state_list[index]

    print("Min value:",minimum)
    print("Min value state:",state)

    return minimum,state
    
    """   
    minimum = float('inf')  # Initialize to positive infinity
    state = ""
    for element in range(0, len(big_list)):
        big_list[element] = float(big_list[element])

    for element in big_list:
        if element < minimum and element > -1:
            minimum = element

    if minimum == float('inf'):  # If minimum is still positive infinity, no valid minimum found
        return None, None

    index = big_list.index(minimum)
    state = state_list[index]
    return minimum, state   
    

def output(head_list, min_state, max_state, min_value, max_value):
    """ This function is going to take 5 headers, values, and states associated with the values.
        Requires: A List of 5 headers, 2 separate state lists, 2 separate value lists. Each containing 5 values.
        Returns: An int(1). """
#This is the function that gave me trouble. In my minimum function, I recieved an error saying that
#'999999' wasn't in the list. I found this issue odd, and NOTHING I did fixed it. Same with max.
#Because of that, the code wouldn't even run. Changing the output function to [i] made it so it read everything rather than
#The first 5 indicators. It doesn't display anything. But it runs. 
    """
    min_value_string = []
    max_value_string = []

    for element in range(0, len(min_value)):
        min_value_string.append((str(min_value[element]) if min_value[element] is not None else ""))
        max_value_string.append((str(max_value[element]) if max_value[element] is not None else ""))

    output_file_obj = open("best_and_worst.txt", 'w')
    print('{:<35}:{:<30}{:<5}'.format("indicator","Min","Max"),file = output_file_obj)
    print('---------------------------------------------------------------------------------------------------------',file=output_file_obj)
    print('{:<35}:{:<30}{:<5}:    {:<20}{:>5}'.format(head_list[0], min_state[0] if min_state[0] is not None else "", min_value_string[0], max_state[0] if max_state[0] is not None else "", max_value_string[0]), file=output_file_obj)
    print('{:<35}:{:<30}{:<5}:    {:<20}{:>5}'.format(head_list[1], min_state[1] if min_state[1] is not None else "", min_value_string[1], max_state[1] if max_state[1] is not None else "", max_value_string[1]), file=output_file_obj)
    print('{:<35}:{:<30}{:<5}:    {:<20}{:>5}'.format(head_list[2], min_state[2] if min_state[2] is not None else "", min_value_string[2], max_state[2] if max_state[2] is not None else "", max_value_string[2]), file=output_file_obj)
    print('{:<35}:{:<30}{:<5}:    {:<20}{:>5}'.format(head_list[3], min_state[3] if min_state[3] is not None else "", min_value_string[3], max_state[3] if max_state[3] is not None else "", max_value_string[3]), file=output_file_obj)
    print('{:<35}:{:<30}{:<5}:    {:<20}{:>5}'.format(head_list[4], min_state[4] if min_state[4] is not None else "", min_value_string[4], max_state[4] if max_state[4] is not None else "", max_value_string[4]), file=output_file_obj)
    output_file_obj.close()
    return 1
    """
    """
    min_value_string = []
    max_value_string = []

    for element in range(0, len(min_value)):
        min_value_string.append((str(min_value[element])))
        max_value_string.append((str(max_value[element])))

    output_file_obj = open("best_and_worst.txt", 'w')
    print('{:<35}:{:<30}{:<5}'.format("indicator","Min","Max"),file = output_file_obj)
    print('---------------------------------------------------------------------------------------------------------',file=output_file_obj)
    print('{:<35}:{:<30}{:<5}:    {:<20}{:>5}'.format(head_list[0],min_state[0],min_value_string[0],max_state[0],max_value_string[0]),file = output_file_obj)
    print('{:<35}:{:<30}{:<5}:    {:<20}{:>5}'.format(head_list[1],min_state[1],min_value_string[1],max_state[1],max_value_string[1]),file = output_file_obj)
    print('{:<35}:{:<30}{:<5}:    {:<20}{:>5}'.format(head_list[2],min_state[2],min_value_string[2],max_state[2],max_value_string[2]),file = output_file_obj)
    print('{:<35}:{:<30}{:<5}:    {:<20}{:>5}'.format(head_list[3],min_state[3],min_value_string[3],max_state[3],max_value_string[3]),file = output_file_obj)
    print('{:<35}:{:<30}{:<5}:    {:<20}{:>5}'.format(head_list[4],min_state[4],min_value_string[4],max_state[4],max_value_string[4]),file = output_file_obj)
    output_file_obj.close()
    return 1
    print("head_list[0]:", head_list[0])
    print("min_state[0]:", min_state[0])
    print("min_value_string[0]:", min_value_string[0])
    print("max_state[0]:", max_state[0])
    print("max_value_string[0]:", max_value_string[0])
    """
    
    min_value_string = []
    max_value_string = []

    for value in min_value:
        min_value_string.append(str(value) if value is not None else "")
    for value in max_value:
        max_value_string.append(str(value) if value is not None else "")

    output_file_obj = open("best_and_worst.txt", 'w')
    print('{:<35}:{:<30}{:<5}'.format("indicator","Min","Max"),file = output_file_obj)
    print('---------------------------------------------------------------------------------------------------------',file=output_file_obj)
    
    for i in range(len(head_list)):
        min_state_value = min_state[i] if min_state[i] is not None else ""
        max_state_value = max_state[i] if max_state[i] is not None else ""
        min_value_value = min_value_string[i]
        max_value_value = max_value_string[i]
        
        print('{:<35}:{:<30}{:<5}:    {:<20}{:>5}'.format(head_list[i], min_state_value, min_value_value, max_state_value, max_value_value), file=output_file_obj)
    output_file_obj.close()
    return 1
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    """Function for running the program."""
    check_input = True
    while check_input == True:
        file_str = input("Enter name of the file to be opened: ")
        try:
            file_object = open(file_str, 'r', encoding= "windows-1252")
            check_input = False
        except FileNotFoundError:
            print("File ",file_str,"doesn't exist.")

    state_list,state_header = make_trim_list(file_object,0)
    file_object.seek(0)
    heart_list,heart_header = make_trim_list(file_object,1)
    file_object.seek(0)
    motor_list,motor_header = make_trim_list(file_object,5)
    file_object.seek(0)
    birth_list,birth_header = make_trim_list(file_object,7)
    file_object.seek(0)
    smoking_list,smoking_header = make_trim_list(file_object,11)
    file_object.seek(0)
    obesity_list,obesity_header = make_trim_list(file_object,13)

    heart_min,min_heart_state = get_min_and_states(heart_list,state_list)
    heart_max,max_heart_state = get_maximums_and_states(heart_list,state_list)

    motor_min,min_motor_state = get_min_and_states(motor_list,state_list)
    motor_max,max_motor_state = get_maximums_and_states(motor_list,state_list)

    birth_min,min_birth_state = get_min_and_states(birth_list,state_list)
    birth_max,max_birth_state = get_maximums_and_states(birth_list,state_list)

    smoking_min,min_smoking_state = get_min_and_states(smoking_list,state_list)
    smoking_max,max_smoking_state = get_maximums_and_states(smoking_list,state_list)

    obesity_min,min_obesity_state = get_min_and_states(obesity_list,state_list)
    obesity_max,max_obesity_state = get_maximums_and_states(obesity_list,state_list)

    headers = [heart_header,motor_header,birth_header,smoking_header,obesity_header]
    min_state_list = [min_heart_state,min_motor_state,min_birth_state,min_smoking_state,min_obesity_state]
    max_state_list= [max_heart_state,max_motor_state,max_birth_state,max_smoking_state,max_obesity_state]
    min_state_values = [heart_min,motor_min,birth_min,smoking_min,obesity_min]
    max_state_values = [heart_max,motor_max,birth_max,smoking_max,obesity_max]

    number = output(headers,min_state_list,max_state_list,min_state_values,max_state_values)
    print("Finished.")
    file_object.close()
main()
    