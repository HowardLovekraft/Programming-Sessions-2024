abc = [int(elem) for elem in input().split()]

abc_sorted = sorted(abc)[::-1]
min_abc, max_abc = min(abc), max(abc)
abc_sliced = abc[::2]

print(abc_sorted)
print(min_abc)
print(max_abc)
print(abc_sliced)

