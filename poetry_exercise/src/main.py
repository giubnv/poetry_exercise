import math

class MyMath:
    def sqrt (self, x):
        pass
    def sin (self, x):
        pass

class ApproxMath(MyMath):
    # Newton-Raphson
    def sqrt(self, x):
        if x < 2:
            return x
        a = 1255
        for i in range(1, 10):
            b = (x / a)
            a = ((a + b) / 2)
        return a

    def sin2pi (self, x):
        # sin of 2 * pi * x
        x = x - math.floor(x)
        xp1 = x + x - 1
        xp2 = math.fabs(xp1)
        xp = 1.570796326794897 - 1.570796326794897 * math.fabs(xp2 + xp2 - 1)
        y = -math.copysign(1, xp1) *(xp + xp * xp * (-0.05738534102710938 - 0.1107398163618408 * xp))
        return y

    def sin(self, x):
        return self.sin2pi(x/(2*math.pi))

class ExactMath(MyMath):

    def sqrt(self, x):
        return math.sqrt(x)
    def sin(self, x):
        return math.sin(x)



if __name__ == '__main__':
    print('ciao')

    mymath_approx = ApproxMath()
    mymath_exact = ExactMath()

    print(mymath_approx.sqrt(100))
    print(mymath_exact.sqrt(100))

    print(mymath_approx.sin(math.pi/3))
    print(mymath_exact.sin(math.pi/3))