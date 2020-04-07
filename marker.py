#!/usr/bin/env python

from result_parser import exam_results

class marker(exam_results):
    def __init__(self, result_path):
        super(marker,self).__init__(result_path)
        self.result_path = result_path
    
    def get_top_score(self, subject):
        self.result_info = self.get_result_info()
        subject_index = self.result_info['subjects'].index(subject)
        subject_max = 0
        for k, v in self.result_info.items():
            if k == "subjects":
                continue
            if v[subject_index] > subject_max:
                subject_max = v[subject_index]
        return subject_max
