## Ashwin Deshpande - 655640269
from _global import *
from document_processor import *
from query_processor import *


class Engine:
    def __init__(self, stemmer_flag=True, stopwords_flag=True, min_word_length=2,
                 document_directory=CRANFIELD_DIRECTORY):
        ###################################################################################################
        ################### Document processor ##################
        # Document processor class handles document vector creation
        self.doc_processor = DocumentProcessor(document_directory=document_directory,
                                               preprocessor=Preprocessor(stopwords_flag=stopwords_flag,
                                                                         stemmer_flag=stemmer_flag,
                                                                         min_word_length=min_word_length))

    def search(self, query):
        query = self.doc_processor.preprocessor.preprocess(query)
        cosine_scores = self.get_cosine(query_tokens=query)
        ranked_docs = sorted(cosine_scores.keys(), key=cosine_scores.get, reverse=True)
        return ranked_docs

    def get_cosine(self, query_tokens):
        query_length = 0
        scores = {}
        for token in set(query_tokens):
            if token not in self.doc_processor.inverted_index:
                continue
            qtoken_tf = query_tokens.count(token)
            idf = self.doc_processor.term_to_idf[token]
            qtoken_tfidf = qtoken_tf * idf
            query_length += qtoken_tfidf ** 2
            for doc_id, dtoken_tfidf in self.doc_processor.inverted_index[token].items():
                if doc_id not in scores:
                    scores[doc_id] = 0
                scores[doc_id] += qtoken_tfidf * dtoken_tfidf
        scores = self.normalize_score(scores, query_length)
        return scores

    def normalize_score(self, scores, query_length):
        normalized_scores = {}
        for doc_id, score in scores.items():
            doc_length = self.doc_processor.document_lengths[doc_id]
            normalized_scores[doc_id] = score / ((query_length * doc_length) ** (1 / 2))
        return normalized_scores
