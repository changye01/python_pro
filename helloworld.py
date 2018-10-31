
a = 100
if a>100:
    print(a)
else:
    print(-a)
print(3<5)
print(True or False)
print(not True)
a=b=c=1
z,x,y=1,2,3
# print a,b,c,x,z,y
print(a,b,c,z,x,y)
if a<z:
    print('1')
elif x<y:
    print('2')
else:
    print('3')
a = 5
b = 3
# /	    除 - x 除以 y
# //	取整除 - 返回商的整数部分 
print (a/b)
# while(1):
#     print('hello world')

var1 = 'hello world'
var2 = 'changye'
# print(var1[0])
# 1:5 从1到5的前一个字符串
# print(var2[1:5])
print(var1[0:6] + 'Runoob!')
list = ['a', 'b', 1]
print(list)
print(abs(-10))
print(1>2)
import math  # 导入 math 模块
# log() 方法返回x的自然对数，x > 0。
print ("math.log(100.12) : ", math.log(100.12))
# modf() 方法返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
print ("math.modf(100.12) : ", math.modf(100.12))

# pow() 方法返回 xy（x的y次方） 的值。
# 函数是计算x的y次方，如果z在存在，则再对结果进行取模，其结果等效于pow(x,y) %z

# 注意：pow() 通过内置的方法直接调用，内置方法会把参数作为整型，而 math 模块则会把参数转换为 float。
print ("pow(100, 2) : ", pow(100, 2))
print ("pow(100, 2) : ", math.pow(100, 2))

# round() 方法返回浮点数x的四舍五入值。
print ("round(70.23456) : ", round(70.23456))
print ("round(56.659,1) : ", round(56.659,1))
# n -- 表示从小数点位数，其中 x 需要四舍五入，默认值为 0。
print ("round(100.000056, 3) : ", round(100.000056, 4))
print ("math.sqrt(100) : ", math.sqrt(100))

import random

print ("from range(100) return a random num : ",random.choice(range(100)))
print ("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print ("从字符串中 'Runoob' 返回一个随机字符 : ", random.choice('Runoob'))

a = "Hello"
b = "Python"
 
print("a + b print:", a + b)
print("a * 2 print:", a * 2)
print("a[1] print:", a[1])
print("a[1:4] print:", a[1:4])
 
if( "H" in a) :
    print("H in a ")
else :
    print("H not in  a ")
 
if( "M" not in a) :
    print("M note in var a ")
else :
    print("M in var a ")
 
print (r'\n')
print (R'\n')

print ("my name is  %s ,i am  %d years old!" % ('littleCat', 10))

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
 
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

print(len(list2))
del list2[2]
print(list2)
print([1, 2, 3] + [4, 5, 6])

print(['Hi!'] * 4)

squares = [1, 4, 9, 16, 25]
squares += [36, 49, 64, 81, 100]
print(squares)

# id() 函数用于获取对象的内存地址。
print(id(squares[0]))
# for x in squares:
    # print id(squares[])
list1 = ['我','爱','python']
list2 = [100, 200, 300]
print( 'list1的最大值:', max(list1) )
print( 'list2的最大值:', max(list2) )
 
# 可以看出列表中元素为字符串的时候，max 函数的比较是根据 id 的大小来判断的。
print( id(list1[0]) )
print( id(list1[1]) )
print( id(list1[2]) )

print('我' > '爱')
print('爱' > 'python')
print('我' > 'python')

tup1 = ('Google', 'Runoob', 1997, 2000)
print ("tup1[0]: ", tup1[1])
print(type(tup1))

# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
tup1 = (50)
print(type(tup1))

tup1 = (50,)
print(type(tup1))

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
 
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
tup3 = tup1 + tup2
print (tup3)


# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup = ('Google', 'Runoob', 1997, 2000)
 
print (tup)
del tup
print ("删除后的元组 tup : ")
print (tup)

 
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8              # 更新 Age
dict['School'] = "ace"  # 添加信息
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
# 输出字典，以可打印的字符串表示。
print(str(dict))
dict.clear()     # 清空字典
del dict         # 删除字典
print(dict)


# 实例中 dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的，dict3 父对象进行了深拷贝，
# 不会随dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改。
dict1 =  {'user':'runoob','num':[1,2,3]}
 
dict2 = dict1          # 浅拷贝: 引用对象
dict3 = dict1.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
 
# 修改 data 数据
dict1['user']='root'
dict1['num'].remove(1)
 
# 输出结果
print(dict1)
print(dict2)
print(dict3)

# 集合（set）是一个无序的不重复元素序列。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(type(basket))
a = set('abracadabra')
b = set('alacazam')
# 集合a中包含元素
print(a - b)
# 集合a或b中包含的所有元素
print(a | b)
# 集合a和b中都包含了的元素
print(a & b)
# 不同时包含于a和b的元素
print(a ^ b)

thisset = set(("Google", "Runoob", "Taobao"))
# 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
thisset.add('linxiansheng')
thisset.add('wula')
thisset.update({1,3})
thisset.update([2,4],[6,5])
print(thisset)

thisset = set(("Google", "Runoob", "Taobao"))
# 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。
thisset.remove('Google')
# 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。
thisset.discard('Taobao')
print(thisset)

thisset = set(("Google", "Runoob", "Taobao"))
print(thisset)
# 清空集合
thisset.clear()
x = thisset.pop()
print(thisset)
print(x)

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

a, b = 0, 1
while b < 1000:
    # 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
    print(b, end=',')
    a, b = b, a+b

age = int(input("请输入你家狗狗的年龄: "))

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("1 to %d sum is: %d" % (n,sum))

count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
   

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

# for i in range(5):
# 以使用range指定区间的值：
# for i in range(5,9) :
# 可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for i in range(0, 10, 3):
# for i in range(-10, -100, -30) :
    print (i)

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print (i,a[i])

# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。

# 还可以使用range()函数来创建一个列表：
# list(range(5))


# 迭代器是一个可以记住遍历的位置的对象。    

# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 字符串，列表或元组对象都可用于创建迭代器
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")

import sys
list=[1,2,3,4]
it = iter(list)
print (next(it))
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()


def area(width, height):
    return width * height
 
def print_welcome(name):
    print("Welcome", name)
 
print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

a=[1,2,3]
a="Runoob"

# 以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅
# 是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。

# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
#!/usr/bin/python3
  
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )

# 加了两个星号 ** 的参数会以字典的形式导入。
def printinfo1(arg1, **vardict ):
    #    "打印任何传入的参数"
    print ("输出: ")
    print (arg1)
    print (vardict)
 
# 调用printinfo 函数
printinfo1(1, a=2,b=3)   

# 如果单独出现星号 * 后的参数必须用关键字传入。
# 不使用的话会报错
def f(a,b,*,c):
    return a+b+c
f(1,2,c=3)