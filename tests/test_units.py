#!/usr/bin/env python

from examine.result_parser import exam_results
from examine.marker import marker


class Test_exam_results:
    def test_no_missing_column(self):
        exm = exam_results("data/missing_column_data.txt")
        assert exm.no_missing_column() == False

    def test_get_result_info(self):
        exm = exam_results("data/sample_exam_results.txt")
        rinfo = exm.get_result_info(sep="\t")
        assert type(rinfo) == dict


def test_marker():
    mkr = marker("data/sample_exam_results.txt")
    assert mkr.get_top_score("Maths") == 100
