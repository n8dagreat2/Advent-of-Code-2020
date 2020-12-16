# Day 2 - Part 2 of Advent of Code 2020
# Objective for this part:
#   Find the total number of valid passwords given the positions the letter is supposed to be in (1 is the begining of the password not 0) and the lines of input from input.txt. Only one of the positions need to be correct and only one needs to be correct in order to be added.
#   Example: 1-3 a: abcde is valid because position 1 contains a and position 2 does not
#            1-3 b: cdefg is not valid because neither position contains the letter b
#            2-9 c: ccccccccc is not valid because both positions contain the letter c

input_file = open("input.txt", "r")
lines = input_file.readlines()        # Saves each line in an array with each index being individual lines

inputs = []                           # Variable used to hold the split inputs
for x in range(len(lines)):
    inputs.append(lines[x].split())   # splits the input lines into their respective parts: [policy criteria, policy letter, password]

total_correct = 0                     # variable used to hold the total number of correct passwords from the input
for i in inputs:
    first = int(i[0].split('-')[0])   # i[0] is the policy, split('-')[0] is the lower bound of the policy
    second = int(i[0].split('-')[1])  # " , split('-')[1] is the upper bound of the policy
    letter = i[1][0]                  # i[1][0] is the letter position for the policy and it is the 0th term in that postion
    password = i[2]
    if password[first - 1] == letter and not password[second - 1] == letter:
        total_correct += 1
    elif not password[first - 1] == letter and password[second - 1] == letter:
        total_correct += 1

print("The total number of correct passwords is: " + str(total_correct))

input_file.close()
