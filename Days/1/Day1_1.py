# Day 1 - Part 1 of Advent of Code 2020
# Objective for this part:
#   Find 2 numbers that add up to 2020 in input.txt and multiply them for the answer

input_file = open("input.txt", "r")
lines = input_file.readlines()   # Saves each line in an array with each index being individual lines

# Change the input array to integer values to be used later
for x in range(len(lines)):
    lines[x] = int(lines[x].strip())

for i in range(len(lines)):
    for j in range(len(lines) - i):
        if(lines[i] + lines[i + j] == 2020):
            total = lines[i] * lines[i + j]
            print("The total is: " + str(total))

input_file.close()
