#Owen Manley, CSC 240, Assignment #6. This program takes two text files and creates a dictionary out of them. Then,
#it is going to compare the files to calculate the total words common in both files and the total number of words 
#occuring in both.
import string 
#--------------------------------------------------------------------------------------------------------------------
def print_index(file):
    """Compile a dictionary of words and line numbers. 
        Print each word in alphabetic order.
        Line numbers in ascending order.
        Key = words, and values = the line numbers.
        Values will be saved in a set. Assume line_number starts at 1."""
    word_dict = {}
    line_num = 1
    
    for line in file: #Split the lines up.
        words = line.split()#Each time loop hits a word, make newline.
        
        for word in words:
            word = word.strip().lower().strip('.?!,:;"')#Strip unnecessary puncuation.
            if word in word_dict:#If the word is in the dictionary, add the line number to it.
                word_dict[word].add(line_num)
            
            else:
                word_dict[word] = {line_num}#Create key/value pair.
        line_num += 1
    pretty_print(word_dict)
#--------------------------------------------------------------------------------------------------------------------       
def pretty_print(word_dict):
    """ Print the dictionary in a pleasing format.
        Sort the keys so it prints in the correct order as stated in print_index. """
     for word in sorted(word_dict.keys()):
        print(word + ':', sorted(word_dict[word]))
 #--------------------------------------------------------------------------------------------------------------------       
def compare_files(file1,file2):
    """ Take both text file objects and compare them using sets (intersection/union)."""
    file_set1 = set(file1.read().lower().split())
    file_set2 = set(file2.read().lower().split())
    common_words = len(file_set1.intersection(file_set2))
    print(f'Words common in both files:\n{common_words}')
    print()
    total_words = len(file_set1 | file_set2)
    print(f'Total number of words that occured in both files:\n{total_words}')    
#--------------------------------------------------------------------------------------------------------------------
def main():
    """ Main function for running the file. Taking both text files as hardcoded for simplicity. """
    file1 = open('gttysBurg.txt','r')
    file2 = open('declarationOfInd.txt','r')
    print('Printing index for gttysBurg.txt...\n')
    print_index(file1)
    print('\nPrinting index for declarationOfInd.txt...\n')
    print_index(file2)

    file1.seek(0) #I couldn't really figure out how to continually print the dictionary because I had to 
                  #reset the file pointers each time. So, I had to look it up, and this was the result.
    file2.seek(0)
    print('\nComparing files of gttysBurg.txt & declarationOfInd.txt...\n')
    compare_files(file1,file2)
    file1.close()
    file2.close()
    