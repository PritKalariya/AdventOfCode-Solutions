with open ('inputs/input_01.txt') as f:
    input = f.readlines()


################################### Part One ###################################
counter = 0

for i in range(1, len(input)):
    if int(input[i]) > int(input[i - 1]):
        counter += 1

print(counter)


################################### Part Two ###################################
set_counter = 0
sets = []

for i in range(2, len(input)):
    addition = int(input[i]) + int(input[i - 1]) + int(input[i - 2])
    sets.append(addition)

for i in range(len(sets)):
    if sets[i] > sets[i - 1]:
        set_counter += 1

print(set_counter)