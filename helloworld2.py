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
##
# 元组
t = 12345, 54321, 'hello!'
print(t)
u = t,[1,2,3,45,5]
print(u)

# 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
# 可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # 删除重复的
print('orange' in basket) 

# 以下演示了两个集合的操作

a = set('abracadabra')
b = set('alacazam')

print(a-b)
print(a|b)
print(a&b)
# 在 a 或 b 中的字母，但不同时在 a 和 b 中
print(a^b)

# 集合也支持推导式：
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# 序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。

# 理解字典的最佳方式是把它看做无序的键=>值对集合。在同一个字典之内，关键字必须是互不相同。

# 一对大括号创建一个空的字典：{}。

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 2029
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)
print(list(tel.keys()))
sorted(tel.keys())

# 构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对：
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

# 此外，字典推导可以用来创建任意键和值的表达式词典：

dict1 = {x: x**2 for x in (2, 4, 6)}
print(dict1)

# 如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便：
dict2 = dict(sape=4139, guido=4127, jack=4098)
print(dict2)


# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)
    
# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)


# 同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('what is your {0}? it is {1} '.format(q,a))

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：

for i in reversed(range(1,10,2)):
    print(i)


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)