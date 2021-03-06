#!/usr/bin/env python

class exam_results(object):
    """Class to parse file and store required info"""
    
    def __init__(self, result_path):
        """Parse the mentioned file"""
        self.result_path = result_path
        
    def get_result_info(self):
        """returns a dict with column header as key"""
        rdict = {}
        with open(self.result_path, "r") as ifl:
            rdict['subjects'] = ifl.readline().strip().split('\t')[1:]
            for st in ifl:
                st = st.strip().split('\t')
                rdict[st[0]] = [int(m) for m in st[1:]]
        return rdict
    
    def no_missing_column(self):
        """Check if given file have all column info for all rows"""
        row_lengths = set()
        with open(self.result_path, "r") as ifl:
            for st in ifl:
                st = st.strip().split('\t')
                row_lengths.add(len(st))
        return len(row_lengths) == 1
            