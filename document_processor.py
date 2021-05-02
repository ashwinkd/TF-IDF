## Ashwin Deshpande - 655640269
from data import *
from preprocessor import *


class DocumentProcessor:
    def __init__(self, document_directory, preprocessor):
        self.preprocessor = preprocessor
        self.data_object = Data(document_directory=document_directory)
        self.inverted_index = {}
        self.term_to_idf = {}
        self.document_lengths = {}
        self.create_inverted_index()

    def create_inverted_index(self):
        self.get_term_frequency()
        self.get_inverse_document_frequency()

    def get_term_frequency(self):
        '''
        Create e dictionary with:
        key: term   ---> Another dictionary:
                        key: doc_id:  ---> number of occurrences
        :return:
        '''
        doc_id, document = self.data_object.get_next_document()
        while document is not None:
            document = self.format_sgml(text=document, fields=CRANFIELD_TAGS)
            self.add_to_index(document, doc_id)
            doc_id, document = self.data_object.get_next_document()

    def get_inverse_document_frequency(self):
        """
        :return:
        """
        for term, document_map in self.inverted_index.items():
            document_frequency = len(document_map)
            inverse_document_frequency = log10(self.data_object.N / document_frequency)
            self.term_to_idf[term] = inverse_document_frequency
            for doc_id, term_frequency in document_map.items():
                tfidf = term_frequency * inverse_document_frequency
                self.inverted_index[term][doc_id] = tfidf
                if doc_id not in self.document_lengths:
                    self.document_lengths[doc_id] = 0
                self.document_lengths[doc_id] += tfidf ** 2

    def format_sgml(self, text: str, fields: list):
        """
        Takes a raw string and return a dictionary with
        key: TITLE or TEXT tag  ---> raw text
        :param text:
        :param fields:
        :return:
        """
        document = {}
        for field in fields:
            try:
                START_TAG = "<" + field + ">"
                END_TAG = "</" + field + ">"
                START = text.index(START_TAG) + len(START_TAG) + 1
                END = text.index(END_TAG)
                value = text[START: END]
                value = self.preprocessor.preprocess(value)
                document[field] = value
            except Exception as err:
                logger.error(err)
                continue
        return document

    def add_to_index(self, document, doc_id):
        """
        Creates a term to doc index
        :param document:
        :param doc_id:
        :return:
        """
        for zone, tokens in document.items():
            for token in tokens:
                if token not in self.inverted_index:
                    self.inverted_index[token] = {}
                if doc_id not in self.inverted_index[token]:
                    self.inverted_index[token][doc_id] = 0
                self.inverted_index[token][doc_id] += 1
