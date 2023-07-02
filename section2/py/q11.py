from util import open_hightemp

text = open_hightemp()

text = text.split("\n")

for line in text:
    replace_space = line.replace("\t"," ")
    print (replace_space)


