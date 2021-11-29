with open ('inputs/input_01.txt') as f:
    input = f.read()


################################### Part One ###################################
print(f"floor = {input.count('(') - input.count(')')}")


################################### Part two ###################################
floor = 0
position = 1

for brace in input:
    if brace == '(':
        floor += 1
    elif brace == ")":
        floor -= 1

    if floor == -1:
        print(f"Basement entered at position = {position}")
        break

    position += 1