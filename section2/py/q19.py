from operator import itemgetter

with open("hightemp.txt", "r") as f:
    temp_lines = f.readlines()



prefecture_dic = {}

 
for line in temp_lines:
    prefecture = line.split("\t")[0]
    if prefecture in prefecture_dic.keys():
        prefecture_dic[prefecture] += 1
    else :
        prefecture_dic[prefecture] = 1

prefecture_dic = sorted(prefecture_dic.items(), key=lambda x: x[1], reverse = True)

print (prefecture_dic)
