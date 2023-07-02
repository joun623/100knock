from random import shuffle 

def make_ramdom_sentence(sentence):
    sentence_list = sentence.strip().split()
    random_sentence_list = []

    for word in sentence_list:
        if len(word) > 4:
            middle_word = list(word[1:-1])
            shuffle(middle_word)
            random_sentence_list.append(word[0] + "".join(middle_word)+ word[-1])
        else :
            random_sentence_list.append (word)

    return " ".join(random_sentence_list)

random_sentence = make_ramdom_sentence("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
print(random_sentence)
