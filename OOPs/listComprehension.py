l = [1, 2, 3, "a"]

# for a in l:
#     print(type(a))

new_l = [a for a in l if type(a) == str]


print(new_l)
