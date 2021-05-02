## Ashwin Deshpande - 655640269
# Document processor class is defined in document_processor.py
from document_processor import *
from query_processor import *
from engine import *
from score import *


def main():
    score_object = Score(GOLD_SEARCH_RESULT_PATH)
    search_engine = Engine()
    ################### Query processor ##################
    # query processor class return queries
    query_processor = QueryProcessor(query_document_path=QUERIES_PATH)
    query_index, query = query_processor.get_next_query()
    while query is not None:
        document_results = search_engine.search(query)
        score_object.set_results(query_index, document_results)
        query_index, query = query_processor.get_next_query()
    score_object.print_scores()


if __name__ == '__main__':
    main()
