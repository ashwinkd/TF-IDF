## Ashwin Deshpande - 655640269
from preprocessor import *


class QueryProcessor:
    def __init__(self, query_document_path):
        self.query_list = self.read_queries(query_document_path)
        self.query_index = 0

    def read_queries(self, document_path):
        file_ptr = open(document_path, 'r')
        return file_ptr.readlines()

    def get_next_query(self):

        if self.query_index >= len(self.query_list) - 1:
            return None, None
        try:
            query = self.query_list[self.query_index]
            self.query_index += 1
            return self.query_index, query
        except Exception as err:
            logger.error(err)
            return None, None
