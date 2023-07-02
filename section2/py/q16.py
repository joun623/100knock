import sys

if len(sys) < 1:
    print ("please input your systems")
    N = input
else :
    N = sys.argv[1]

with open("hironsan.txt") as f:
    line = f.readlines()

split_num = len(line) / int(N)

for index in range(0, len(line), split_num):
    with open("hironsan_split" + index + ".dat") as fout:
        fout.write(line[index:index+split_num])


