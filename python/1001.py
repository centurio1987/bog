from functools import reduce

print(reduce(lambda n, acc: n - acc, map(int, input().split())))