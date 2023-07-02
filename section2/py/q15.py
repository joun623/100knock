from util import open_hightemp

text = open_hightemp()

line_num = input()

print ("\n".join(text.split("\n")[-line_num - 1:]))
