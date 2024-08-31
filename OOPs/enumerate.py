l = [1,2, 3, 4, 5]
idx = 0

for a in l:
    print("idx", idx)
    print(a)
    idx = idx + 1

for idx, a in enumerate(l):
    print("enum_idx", idx)
    print(a)