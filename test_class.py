class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    # 定义一个默认的显示类的方法
    def __str__(self):
        return str(self.num)+"/"+str(self.den)


myf = Fraction(3, 5)
print(myf)
print("I ate", myf, "of the pizza")
print(myf.__str__())
print(str(myf))
