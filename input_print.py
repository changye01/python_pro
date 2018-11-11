# Python两种输出值的方式: 表达式语句和 print() 函数。
# 第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
# str()： 函数返回一个用户易读的表达形式
# 如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
# repr()： 产生一个解释器易读的表达形式。
# 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。

s = 'Hello, Runoob'
print(str(s))
print(repr(s))

#   repr() 函数可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)


# repr() 的参数可以是 Python 的任何对象
x = 10 * 3.25
y = 200 * 200
x = repr((x, y, ('Google', 'Runoob')))
print(x)



# 这里有两种方式输出一个平方与立方的表:s
# 字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end='x')
 # 注意前一行 'end' 的使用
    print(repr(1).rjust(3))


# 还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
# 另一个方法 zfill(), 它会在数字的左边填充 0，如下所示：
x = '12'.zfill(5)
print(x)


# str.format() 的基本使用如下:
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

print("aa{},aa{}".format('2',3))

# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
# 位置及关键字参数可以任意的结合:

print('{name}网址： {site}'.format(site='www.runoob.com',name='菜鸟教程' ))

# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。

# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:8} ==> {1:10d}'.format(name, number))

# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。/
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

# 也可以通过在 table 变量前使用 '**' 来实现相同的功能：
# **会以字典的格式到处
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))


# 旧式字符串格式化
# % 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串. 例如

import math
print('常量 PI 的值近似为：%5.3f。' % math.pi)

str1 = input("请输入：")
print("你输入的内容是: ", str1)