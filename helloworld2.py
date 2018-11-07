matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# res = [[row[i] for row in matrix] for i in range(4)]
res = [[row for row in matrix] for i in range(4)]
# res = [i for i in range(4)]
print(res)
# 使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。这与使用 pop()
#  返回一个值不同。可以用 del 语句从列表中删除一个切割，或清空整个列表
#  （我们以前介绍的方法是给该切割赋一个空列表）


a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del(a[2:4])
#清空a
del(a[:])
print(a)
del a

#a以删除 会报错
print(a)