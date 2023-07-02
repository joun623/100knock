str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

elements_list = str.split(" ")

index = [1, 5, 6, 7, 8, 9, 15, 16, 19]

elements_symbol = {}

for sub in range(len(elements_list)):
    add_index = 1 if sub + 1 in index else 2
    elements_symbol[elements_list[sub][0:add_index]] = sub 

print (elements_symbol)	
