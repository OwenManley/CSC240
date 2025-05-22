{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "bb44db10-46d5-44d3-9af1-8930055ec137",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#Owen Manley, CSC 240, Assignment 4. This assignment uses the doc strings provided to solve the problems of two functions.\n",
    "def get_and_strip_number(s):\n",
    "    \"\"\"Requires:\n",
    "       -- string s consists of (the string representing) a non-negative integer n followed\n",
    "          by a single space, and then n words, separated by a single space\n",
    "       Returns:\n",
    "       -- the leading integer n (as an int), and\n",
    "       -- the \"rest\" of s, i.e., what is left after stripping off n and, if n>0,\n",
    "          the space following it\"\"\"\n",
    "    # replace this comment and the next statement with your function body\n",
    "    \n",
    "    #While a goes through the string and finds a number:\n",
    "    a = 0\n",
    "    while a < len(s) and s[a].isdigit():\n",
    "        a += 1\n",
    "#-----------------------------------------------------------------------\n",
    "#When the number is found, use splicing to split the number and print the rest of the string.\n",
    "    num = int(s[:a])\n",
    "    remaining_string = s[a:].strip()\n",
    "    \n",
    "    return num, remaining_string\n",
    "    \n",
    "\n",
    "def get_and_strip_word(s):\n",
    "    \"\"\"Requires:\n",
    "       -- string s has no leading spaces, and is either empty or\n",
    "          consists of one or more words, separated by a single space\n",
    "       Returns:\n",
    "       -- first word of s, and\n",
    "       -- the \"rest\" of s, i.e. what is left after stripping off the word and, if\n",
    "          there is one, the space following the word\"\"\"\n",
    "    # replace this comment and the next statement with your function body\n",
    "    #return '', ''\n",
    "    \n",
    "    #while the string doesn't have a space, iterate through it.\n",
    "    b = 0\n",
    "    while b < len(s) and s[b] != ' ':\n",
    "        b += 1\n",
    "    #If there is no space, return the string.\n",
    "    if b == len(s):\n",
    "        return s, ''\n",
    "    #If there is a space, use splicing to split the first word and print the rest of the string.\n",
    "    else:\n",
    "        word = s[:b]\n",
    "        remaining_string = s[b + 1:].strip()\n",
    "    return word, remaining_string\n",
    "        \n",
    "    \n",
    "    \n",
    "def pad_words(s, num_words, final_len):\n",
    "    \"\"\"Requires:\n",
    "       -- final_len > len(s)\n",
    "       -- string s consists of num_words words, each separated by a single space\n",
    "       Returns:\n",
    "       -- string r, containing the words in s evenly padded with spaces to make\n",
    "          len(r) == final_len\"\"\"\n",
    "    if num_words <= 1:      # best we can do is fill out the line with spaces\n",
    "        return s + ((final_len - len(s))*' ')\n",
    "\n",
    "    # there are at least 2 words, so at least one pigeon hole to fill (with spaces)\n",
    "    num_pigeon_holes = num_words - 1                        # the buckets (pigeon holes) are between words\n",
    "    num_pigeons = final_len - (len(s) - num_pigeon_holes)   # my pigeons are spaces\n",
    "    pad_num = num_pigeons // num_pigeon_holes\n",
    "    extra_num = num_pigeons % num_pigeon_holes              # number of holes that get an extra pigeon\n",
    "    working_str = ''\n",
    "    \n",
    "    # take care of the first num_pigeon_holes - extra_num holes\n",
    "    for i in range(num_pigeon_holes - extra_num):\n",
    "        word, s = get_and_strip_word(s)\n",
    "        working_str += word + (pad_num * ' ')   # insert pad_num spaces\n",
    "\n",
    "    # take care of the last extra_num holes\n",
    "    for i in range(extra_num):\n",
    "        word, s = get_and_strip_word(s)\n",
    "        working_str += word + ((pad_num + 1) * ' ')\n",
    "\n",
    "    working_str += s\n",
    "    return working_str\n",
    "\n",
    "def main():\n",
    "    \"\"\"Main program for testing some text formatting functions.\"\"\"\n",
    "    file_name = input(\"Enter the name of the input file: \")\n",
    "    file_obj = open(file_name, \"r\")\n",
    "\n",
    "    print(\"Line length should be as long as the longest line to print, or longer.\") \n",
    "    line_len = int(input(\"Enter the desired line length: \"))\n",
    "    print()\n",
    "\n",
    "    for line in file_obj:\n",
    "        line = line.strip()                   # strip the trailing '\\n'\n",
    "        n, words = get_and_strip_number(line)\n",
    "        print(pad_words(words, n, line_len))\n",
    "\n",
    "    file_obj.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "3bee3dda-7d7e-4a0a-af2c-8acbf7052bc5",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the name of the input file:  testFile.txt\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Line length should be as long as the longest line to print, or longer.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the desired line length:  17\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "This is  a  small\n",
      "test         file\n",
      "for              \n",
      "you to play with.\n",
      "                 \n",
      "The          end.\n",
      "                 \n"
     ]
    }
   ],
   "source": [
    "main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "448058b0-fb7b-4eb8-bba2-2c21dfa438ba",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the name of the input file:  gttysBurg.txt\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Line length should be as long as the longest line to print, or longer.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the desired line length:  61\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "FOUR  SCORE  AND  SEVEN  YEARS  AGO   OUR   FATHERS   BROUGHT\n",
      "FORTH  ON  THIS  CONTINENT  A   NEW   NATION   CONCEIVED   IN\n",
      "LIBERTY  AND  DEDICATED  TO  THE  PROPOSITION  THAT  ALL  MEN\n",
      "ARE                      CREATED                       EQUAL.\n",
      "                                                             \n",
      "NOW WE ARE ENGAGED IN  A  GREAT  CIVIL  WAR  TESTING  WHETHER\n",
      "THAT NATION OR ANY NATION SO CONCEIVED AND SO  DEDICATED  CAN\n",
      "LONG ENDURE. WE ARE MET ON A GREAT BATTLEFIELD OF  THAT  WAR.\n",
      "WE HAVE COME TO DEDICATE A PORTION OF THAT FIELD AS  A  FINAL\n",
      "RESTING PLACE FOR  THOSE  WHO  HERE  GAVE  THEIR  LIVES  THAT\n",
      "THAT             NATION              MIGHT              LIVE.\n",
      "                                                             \n"
     ]
    }
   ],
   "source": [
    "main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eabffa64-c437-4d96-be38-5ea821ab7e2a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
