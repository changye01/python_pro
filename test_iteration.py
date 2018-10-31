class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
#  StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完
# 成指定循环次数后触发 StopIteration 异常来结束迭代。

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

# 定义self.a变量会绑定在对象，函数调用后，不会被销毁；
# 定义a只是局部变量，函数调用完后会被销毁。
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
