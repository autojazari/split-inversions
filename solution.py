#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Sam Mohamed
This module counts the number of ``Split Inversions`` in a given array.
An array can be passed to the module in a text file where each ith element
corresponds to each ith line in the file.

This module has been tested with python 2.7 and python 3.6

Usage:
    $ python3 solution.py array.txt

Arguments:
    filepath: path to file containing array elements

Attributes:
"""
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")

    return parser.parse_args()

def loadfile(filepath):
    with open(filepath) as inputfile:
        return [int(x) for x in inputfile.readlines()]

def merge_and_count(x, y, result, count):
    i, j = 0, 0

    while i < len(x) and j < len(y):
        if x[i] > y[j]:
            result.append(y[j])
            j += 1
            count += len(x) - i 
        else:
            result.append(x[i])
            i += 1

    result += x[i:]
    result += y[j:]

    return result, count

def sort_and_count(array):
    if len(array) == 1:
        return array, 0

    count = 0
    result = []
    
    mid = len(array)//2

    x = array[:mid]
    y = array[mid:]

    x, c1 = sort_and_count(x)
    y, c2 = sort_and_count(y)

    result, c3 = merge_and_count(x, y, result, count)

    return result, (c1+c2+c3)

def main():
    args = parse_args()
    array = loadfile(args.filepath)
    # sanity check
    print("file contains", len(array), "elemnts")

    array = [1,3,5,2,4,6]
    result, count = sort_and_count(array)
    print("there are", count, "split inversion")
    print(result)

if __name__ == '__main__':
    main()