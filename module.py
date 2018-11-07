import sys
# import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
# sys模块包含了与Python解释器和它的环境有关的函数。
# 当Python执行import sys语句的时候，它在sys.path变量中所列目录中寻找sys.py模块。如果找到了这个文件，这个模块的主块中的语句将被运行
# 另外，“sys”是“system”的缩写。

print('command line arg like this:')
for i in sys.argv:
    print(i)
print('\n\nPython pwd is : ', sys.path, '\n')
# sys.argv 是一个包含命令行参数的列表。
# sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表

import module2
module2.print_func('world')

# 一个模块只会被导入一次，不管你执行了多少次import。