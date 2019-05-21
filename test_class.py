class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    # 定义一个默认的显示类的方法
    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum / common, newden / common)

    def __eq__(self, otherfraction):
        return self.num * otherfraction.den == otherfraction.num * self.den

    def __mul__(self, otherfraction):
        newNum = self.num * otherfraction.num
        newDen = self.den * otherfraction.den
        return Fraction(newNum, newDen)

    def __truediv__(self, otherfraction):
        newNum = self.num * otherfraction.den
        newDen = self.den * otherfraction.num
        common = gcd(newNum, newDen)
        return Fraction(newNum / common, newDen / common)

    def __radd__(self, otherfraction):
        return self + otherfraction

    def __iadd__(self, other):
        self = self + other
        return self


def gcd(m, n):
    if n == 0:
        return m
    r = m % n
    return(gcd(n, r))


# myf = Fraction(3, 5)
# print(myf)
# print("I ate", myf, "of the pizza")
# print(myf.__str__())
# print(str(myf))
# myf = Fraction(1, 4) + Fraction(1, 2)
# print(myf)
print(Fraction(1, 3) .__radd__(Fraction(1, 3)))
