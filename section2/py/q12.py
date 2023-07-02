from util import open_hightemp

text = open_hightemp()

text = text.strip().split("\n")

column1 = []
column2 = []

for line in text:
    replace_space = line.split("\t")
    column1.append(replace_space[0])
    column2.append(replace_space[1])

with open("py/col1.txt", "w") as fcol1:
    for row in column1:
        fcol1.write(row + "\n")

with open("py/col2.txt", "w") as fcol2:
    for row in column2:
        fcol2.write(row + "\n")
