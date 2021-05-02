## Ashwin Deshpande - 655640269
from _global import *


class Data:
    def __init__(self, document_directory):
        self.document_directory = document_directory
        self.document_index = -1
        self.documents = []
        self.list_documents()
        self.N = len(self.documents)

    def list_documents(self):
        '''
        Lists all the documents in given directory
        :return:
        '''
        self.documents = sorted([f for f in listdir(self.document_directory)
                                 if isfile(join(self.document_directory, f))])

    def get_next_document(self):
        '''
        Returns document one by one
        :return:
        '''
        if self.document_index >= len(self.documents) - 1:
            return None, None
        self.document_index += 1
        document_name = self.documents[self.document_index]
        document_path = join(self.document_directory, document_name)
        try:
            file_pointer = open(document_path, 'r')
            text = file_pointer.read()
            return self.create_doc_id(document_name), text
        except FileNotFoundError as err:
            logger.error(err)
            return None, None

    def create_doc_id(self, document_name):
        """
        Creates integer id for Cramfield documents
        :param document_name:
        :return:
        """
        doc_id = re.sub("[^0-9]", '', document_name)
        return int(doc_id)
