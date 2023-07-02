from util import open_hightemp

text = open_hightemp()

line_num = input()

print ("\n".join(text.split("\n")[0:int(line_num)]))
