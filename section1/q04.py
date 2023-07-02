str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

elements_list = str.split(" ")

index = [1, 5, 6, 7, 8, 9, 15, 16, 19]

elements_symbol = {}

'''
for word in elements_list:
    if str.index(word) + 1 in index:
        elements_symbol[word] = str.index(word)
    else :
        elements_symbol[word] = str.index(word)
'''

for sub in range(len(elements_list)):
    if sub + 1 in index:
        elements_symbol[elements_list[sub][0]] = sub 
    else :
        elements_symbol[elements_list[sub][0:2]] = sub 

print (elements_symbol)	
