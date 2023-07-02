from util import open_hightemp

col1 = []
with open("py/col1.txt", "r") as fcol1:
    col1 = fcol1.read()

col2 = []
with open("py/col2.txt", "r") as fcol2:
    col2 = fcol2.read()

for c1, c2 in zip(col1.split("\n"), col2.split("\n")):
    print (c1 + " : " + c2)
