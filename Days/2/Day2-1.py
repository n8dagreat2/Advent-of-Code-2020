# Day 2 - Part 1 of Advent of Code 2020
# Objective for this part:
#   Find the total number of valid passwords given the policy (minimum number of letters allowed, maximum number of letters allowed, and the letter the policy refers to) followed by the password in input.txt

input_file = open("input.txt", "r")
lines = input_file.readlines()        # Saves each line in an array with each index being individual lines

inputs = []                           # Variable used to hold the split inputs
for x in range(len(lines)):
    inputs.append(lines[x].split())   # splits the input lines into their respective parts: [policy criteria, policy letter, password]

total_correct = 0                     # variable used to hold the total number of correct passwords from the input
for i in inputs:
    minimum = int(i[0].split('-')[0]) # i[0] is the policy, split('-')[0] is the lower bound of the policy
    maximum = int(i[0].split('-')[1]) # " , split('-')[1] is the upper bound of the policy
    letter = i[1][0]                  # i[1][0] is the letter position for the policy and it is the 0th term in that postion
    password = i[2]
    if password.count(letter) >= minimum and password.count(letter) <= maximum:
        total_correct += 1

print("The total number of correct passwords is: " + str(total_correct))

input_file.close()
