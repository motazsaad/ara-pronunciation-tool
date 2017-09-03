#!/usr/bin/python
# -*- coding: UTF8 -*-

import sys


def distinct(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

inputFileName = sys.argv[1]
inputFile = open(inputFileName, mode='r', encoding='utf-8')
utterances = inputFile.read().splitlines()
inputFile.close()

utterances = sorted(distinct(utterances))

inputFile = open(inputFileName, mode='w', encoding='utf-8')
inputFile.write("\n".join(utterances) + '\r\n')
inputFile.close()
