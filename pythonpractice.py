import math
import typing

def is_isogram(string):
    print(set(string.lower()))
    print(len(set(string.lower())))
    print(len(string))

# is_isogram("hello")
x = [1,2,3]
y = ["a", "b", "c"]
z = [1,2,3,4,5,6,7,8,9]
yy = [9,8,7,6,5,4,3,2,1]
zz = ["aaa", "bb", "c"]
# print(x.to_bytes(1, "little"))
# print([1,2,3].__iter__().__next__())
# print (x * 2)
# print (x[::2])
# print(min(y))
# print(max(y))
# print("b" in y)
# print(y.index("b", 1))
# print(z)
# del z[::2]
# z.insert(3, "farts")
# xx = z.reverse() this doesn't work
xx = [x for x in z if x % 2 == 0]
# print(xx)
# zz.sort(key=len)
# print(zz)
xxx = tuple(yy)
# print(yy)
# print(xxx[2])
# for num in xxx:
#     print(num)
# for i in range(len(z)):
#     z[i] = i
# print(z)
# zzz = "butterfingers"
# aaa = "nutterbutter"
# print(set(zzz))
# print(set(zzz) & set(aaa))
# if "i" in set(zzz):
#     print(zzz)
q = {
    "hello": "world",
    "goodbye": "dave",
    "wall": "flower",
    "big": "night"
}
print(list(q))
print("wall" in q)
print(q.items())

strings = ["hello", "goodbye", "good morning", "good night"]
print("".join(strings))
print(q.values())
print(list(q.values()))
print(list(q)[list(q.values()).index("dave")])

def find_a_key(dictionary: dict, val: str) -> str:
    return list(dictionary)[list(dictionary.values()).index(val)]

print(find_a_key(q, "flower"))
print(dict(yy))