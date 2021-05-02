## Ashwin Deshpande - 655640269
class Score:
    def __init__(self, target_path):
        self.query_to_doc = self.get_target_dict(target_path)
        self.results = {}

    def set_results(self, query_index, query_results):
        self.results[query_index] = query_results

    def precision_recall(self, pred, target):
        truePositive = target.intersection(pred)
        precision = len(truePositive) / len(pred)
        recall = len(truePositive) / len(target)
        return precision, recall

    def get_target_dict(self, target_path):
        query_to_doc = {}
        file_ptr = open(target_path, 'r')
        for line in file_ptr.readlines():
            q_num, doc_id = [int(t) for t in line.split()]
            if q_num not in query_to_doc:
                query_to_doc[q_num] = set()
            query_to_doc[q_num].add(doc_id)
        return query_to_doc

    def print_scores(self):
        num_queries = len(self.results)
        for top in [10, 50, 100, 500]:
            total_pr, total_re = 0, 0
            for q_index, q_results in self.results.items():
                q_target = self.query_to_doc[q_index]
                pr, re = self.precision_recall(pred=q_results[:top],
                                               target=q_target)
                total_pr += pr
                total_re += re
            total_pr /= num_queries
            total_re /= num_queries
            print("\nTop {} documents:\n\tPrecision: {}\n\tRecall: {}".format(top, total_pr, total_re))
