from operator import itemgetter

with open("hightemp.txt", "r") as f:
    temp_lines = f.readlines()

temp_list = list(map(lambda s : s.split("\t"), temp_lines))
temp_list.sort(key=itemgetter(2))
print (temp_list)
