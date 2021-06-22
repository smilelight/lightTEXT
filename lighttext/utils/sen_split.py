# -*- coding: utf-8 -*-
import re

split_re = re.compile('([﹒﹔﹖﹗．；。！？]["’”」』]{0,2}|：(?=["‘“「『]{1,2}|$))')


def split_sentence(sentence: str):
    lst = []
    for i in split_re.split(sentence):
        if split_re.match(i) and lst:
            lst[-1] += i
        elif i:
            lst.append(i)
    return lst
