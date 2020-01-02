# coding: utf8

import random
from nltk.corpus import movie_reviews


def load(max_examples=None):
    sentences = []
    classes = []

    ids = list(movie_reviews.fileids())
    random.shuffle(ids)

    for fd in ids:
        if fd.startswith("neg/"):
            cls = "neg"
        else:
            cls = "pos"

        fp = movie_reviews.open(fd)
        sentences.append(fp.read())
        classes.append(cls)

        if max_examples and len(classes) >= max_examples:
            break

    print("Sentences:", len(sentences))

    return sentences, classes
