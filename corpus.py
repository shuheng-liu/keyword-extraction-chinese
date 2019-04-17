import os
from document import Document
from stopwords import DEFAULT_STOPWORDS
from gensim.corpora import Dictionary
import numpy as np
import pandas as pd
import nltk
import jieba

DEFAULT_ALLOWED_EXTENSIONS = ['txt']
DEFAULT_CORPUS_PATH = "dataset/corpus"


class Corpus:
    def __init__(self, path, extensions=DEFAULT_ALLOWED_EXTENSIONS, stopwords=None, puncts=None):
        if not os.path.isdir(path):
            raise IOError("{} is not a directory".format(path))

        filenames = [f for f in os.listdir(path) if "." in f and f.rsplit(".")[-1] in extensions]
        self.documents = [Document(os.path.join(path, f), stopwords=stopwords, puncts=puncts) for f in filenames]
        self.tokens = [doc.tokens for doc in self.documents]
        self.ids = None
        self.dictionary = Dictionary(self.tokens)
        self.set_ids()

    def set_ids(self):
        for document in self.documents:
            document.set_ids(self.dictionary)
        self.ids = [doc.ids for doc in self.documents]


if __name__ == '__main__':
    corpus = Corpus(DEFAULT_CORPUS_PATH, stopwords=DEFAULT_STOPWORDS)