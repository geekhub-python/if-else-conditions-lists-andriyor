#!/usr/bin/env python3

l = [int(i) for i in input().split()]
for i in range(1, len(l)):
    if l[i - 1] > 0 and l[i] > 0 or l[i - 1] < 0 and l[i] < 0:
        print(l[i-1], l[i])
        break
