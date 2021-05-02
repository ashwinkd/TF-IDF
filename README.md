# ASSIGNMENT 2
## Ashwin Deshpande - 655640269
## Execution

    > python main.py

## Files
* main.py
    * Contains main function that initiates the execution
* preprocessor.py
    * Contains Preprocessor class that has the follwoing functions:
        * Remove punctuation
        * Tokenize text
        * Remove stopwords
        * Stem words to base form    
* document_processor.py
    * Creates inverted index with each word in vocab as key, and value is a dict of doc_id and term frequency pairs
* query_processor.py
    * Reads queries
* engine.py
    * Gives ranked documents for each query.
    * using Cosine similarity
    * search() returns a list of ranked documents
* score.py
    * Gets Precision and Recall with predicted list of documents and target list of documents (from relevance.txt) 
* data.py
    * Contains Data class that is responsible for listing and reading documents
* _global.py
    * Contains code written in the global field: imports and logging
* _variable.py
    * global variable are defined here.
* log_file.log
    * Contains logging output
* stopwords.txt
    * Contains list of stopwords
    
## Libaries

Requires numpy and NLTK

## Results

* Top 10 documents:
	* Precision: 0.2
	* Recall: 0.18470760233918126
* Top 50 documents:
	* Precision: 0.098
	* Recall: 0.4223976608187135
* Top 100 documents:
	* Precision: 0.06799999999999999
	* Recall: 0.5384210526315789
* Top 500 documents:
	* Precision: 0.0234
	* Recall: 0.9375