with open("hightemp.txt", "r") as f:
    tmp_lines = f.readlines()

prefecture = set()
for line in tmp_lines: 
    prefecture.add(line.split("\t")[0])

print (prefecture)
