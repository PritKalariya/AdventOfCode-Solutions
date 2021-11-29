with open('inputs/input_03.txt') as f:
    input = f.read().strip()


################################### Part One ###################################
def santa():
    visited = set()
    x = 0
    y = 0
    visited.add((x, y))
    for char in input:
        if char == '>':
            x += 1
        elif char == 'V' or char == 'v':
            y += 1
        elif char == '<':
            x -= 1
        elif char == '^':
            y -= 1
        visited.add((x, y))
    print(len(visited))


################################### Part Two ###################################\
def robot_santa():
    visited = set()
    x = 0
    y = 0
    a = 0
    b = 0
    visited.add((x, y))

    for i in range(len(input)):
        char = input[i]
        if i%2 == 0:
            if char == '>':
                a += 1
            elif char == 'V' or char == 'v':
                b += 1
            elif char == '<':
                a -= 1
            elif char == '^':
                b -= 1
            visited.add((a, b))
        else:
            if char == '>':
                x += 1
            elif char == 'V' or char == 'v':
                y += 1
            elif char == '<':
                x -= 1
            elif char == '^':
                y -= 1
            visited.add((x, y))
    print(len(visited))


santa()
robot_santa()