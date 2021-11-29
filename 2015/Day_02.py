with open('inputs/input_02.txt') as f:
    input = f.read()

input = input.split()
paper_needed = 0
ribbon_needed = 0

################################### Part One ###################################
for line in input:
    l, w, h = [int(i) for i in line.split('x')]

    area = (2*l*w) + (2*w*h) + (2*h*l)
    extra_paper = min(l*w, w*h, h*l)

    paper_needed += area + extra_paper           # This is for a single gift.


################################### Part Two ###################################\
    wrapper = min(l+l+w+w, l+l+h+h, w+w+h+h)
    bow = l*w*h

    ribbon_needed += wrapper + bow


print(f'Total Paper needed = {paper_needed}')
print(f'Total Ribbon needed = {ribbon_needed}')