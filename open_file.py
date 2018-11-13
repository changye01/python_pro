f = open('dog.py',"r",encoding='UTF-8')
str1 = f.read()
print(str1)

f.close()


# f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。

f = open('dog.py',"r",encoding='UTF-8')
str1 = f.readline()
print(str1)

f.close()


# f.readlines()
# f.readlines() 将返回该文件中包含的所有行。

# 如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。

# 一种方式是迭代一个文件对象然后读取每行:
f = open('dog.py',"r",encoding='UTF-8')
for line in f:
    print(line, end = '')
f.close()

# 这个方法很简单, 但是并没有提供一个很好的控制。 因为两者的处理机制不同, 最好不要混用。
f = open('testInput.txt',"w",encoding='UTF-8')
num = f.write('I am learning python ,please tell me is write success')
print(num)
f.close()

# 如果要写入一些不是字符串的东西, 那么将需要先进行转换:

f = open('testInput.txt',"a+",encoding='UTF-8')
# num = f.write('I am learning python ,please tell me is write success')
value = ('www.one.com', 14)
s = str(value)
f.write(s)
f.close()




########################## open_file1.py ##############





# 如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
f = open('testInput.txt',"rb+")
x = f.seek(5)
print(x)
line = f.readline()
print(line)
f.close()
# seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
# seek(x,1) ： 表示从当前位置往后移动x个字符
# seek(-x,2)：表示从文件的结尾往前移动x个字符
f = open('testInput.txt',"rb+")
x = f.seek(5,1)
line = f.readline()
print(line)

# 在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。

# 当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。



# 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短:
with open('testInput.txt',"r",encoding="utf-8") as f:
    read_data = f.read()
print(f.closed)