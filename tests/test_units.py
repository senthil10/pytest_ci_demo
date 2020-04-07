#!/usr/bin/env python

from examine.result_parser import exam_results
from examine.marker import marker

exm = exam_results("data/sample_exam_results.txt")
mkr = marker("data/sample_exam_results.txt")

def test_exam_results():
    assert exm.no_missing_column() == True

def test_marker():
    assert mkr.get_top_score("Maths") == 100
