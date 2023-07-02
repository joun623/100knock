def get_ngram(sentence, n=2):
    n_gram = []
    for index in range(len(sentence) - n + 1):
        n_gram.append(sentence[index : index + n])

    return n_gram 

