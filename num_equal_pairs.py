#!/usr/bin/env python3

l = input().split()
pairs = 0
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] == l[j]:
            pairs += 1
print(pairs)

