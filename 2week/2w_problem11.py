import numpy as np


def make_pairs(c):
    for i in range(len(c) - 1):
        yield c[i], c[i + 1]


text = open('che.txt', encoding='utf8').read()
corpus = text.split()
pairs = make_pairs(corpus)

word_dict = {}
for word1, word2 in pairs:
    if word1 in word_dict.keys():
        word_dict[word1].append(word2)
    else:
        word_dict[word1] = [word2]

first_word = np.random.choice(corpus)
while first_word.islower():
    first_word = np.random.choice(corpus)

chain = [first_word]
n_words = 100
for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

print((' '.join(chain)))