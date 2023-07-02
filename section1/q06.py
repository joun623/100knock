from q05 import get_ngram

str1 = "paraparaparadise"
str2 = "paragraph"

X = get_ngram(str1, 2)
Y = get_ngram(str2, 2)

print (set(X) | set(Y))
print (set(X) & set(Y))
print (set(X) - set(Y))

print ("se" in X)
print ("se" in Y)
