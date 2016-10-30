#!/usr/bin/env python3

n = int(input())
m = int(input())
k = int(input())
if (not (k % n) or not (k % m)) and (n * m >= k):
    print('YES')
else:
    print('NO')
