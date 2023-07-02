import re

def cipher(sentence):
    cipher_word = ""
    for c in sentence :
        cipher_word += str(219 - ord(c)) if re.match("[a-z]", c) else c
    
    return cipher_word


print (cipher("Hello my name is Takahashi. My birth day is June 23"))
