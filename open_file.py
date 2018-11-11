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

        