#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# recombination.py
# 2017/05/25(Thu)
# walkingmask

# Use recursive processing to enumerate combinations of sequence A

def recombination(A, n, pos, Asub, combinations, padding=[]):
  if pos == n:
    combinations.append(Asub)
    return
  recombination(A, n, pos+1, Asub+[A[pos]], combinations, padding)
  recombination(A, n, pos+1, Asub+padding, combinations, padding)

if __name__ == "__main__":
  #A = list(map(int, input().split())) # using input
  A = [9, 32, 122, 83, 711, 90, 387] # using writen list
  n = len(A)
  combinations = []
#  recombination(A, n, 0, [], combinations) # no padding
  recombination(A, n, 0, [], combinations, [0]) # zero padding
  for combination in combinations:
    print(combination)
