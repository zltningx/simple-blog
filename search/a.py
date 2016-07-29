#!/usr/bin/env python
# coding=utf-8

write = [3, 14, 17, 22, 24, 26, 31, 36, 37, 39]

with open("T_YX_XSXX.csv.21", 'r') as f:
    with open('a.txt', 'a') as a:
        for line in f:
            line = line.split(',')
            for i, l in enumerate(line):
                if i in write:
                    a.write(l)
                    a.write(",")
            a.write("\n")