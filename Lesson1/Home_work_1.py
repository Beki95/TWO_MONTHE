class Fraction:

    def __init__(self, fraction, fraction2):
        self.fraction = fraction
        self.fraction2 = fraction2

    def dont_znam(self, m, f1):
        m1 = m
        while True:
            if m1 % f1 == 0:
                num = m1
                break
            else:
                m1 += m

        first = num // m
        two = num // f1
        return first, two, num

    def dont_num(self, n1, n2):
        count = 0
        for i in range(1, n1 + 1):
            if n1 % i == 0 and n2 % i == 0:
                if count < i:
                    count = i
        if count != 1:
            return count
        else:
            return None

    def prosto(self, f, f2, fraction1, fraction2):
        ret = None
        ret1 = None
        if f == fraction2:
            f, fraction2 = 1, 1
        else:
            ret1 = self.dont_num(f, fraction2)
        if f2 == fraction1:
            f2, fraction1 = 1, 1
        else:
            ret = self.dont_num(f2, fraction1)
        if ret is None:
            pass
        else:
            fraction1 //= ret
            f2 //= ret
        if ret1 is None:
            pass
        else:
            f //= ret1
            fraction2 //= ret1
        result = f * fraction1, f2 * fraction2
        return result

    def add(self, f, f2):
        if self.fraction2 == f2:
            num = self.fraction + f
            return num, f2
        else:
            res = self.dont_znam(self.fraction2, f2)

            result_first = self.fraction * res[0] + f * res[1]
            return result_first, res[2]

    def subtract(self, f, f2):
        if self.fraction2 == f2:
            num = self.fraction - f
            return num, f2
        else:
            res = self.dont_znam(self.fraction2, f2)
            result_first = self.fraction * res[0] - f * res[1]
            return result_first, res[2]

    def delete(self, f, f2):
        f, f2 = f2, f
        return self.prosto(f, f2, self.fraction, self.fraction2)

    def multiply(self, f, f2):
        return self.prosto(f, f2, self.fraction, self.fraction2)


a = Fraction(2, 6)
print(a.add(2, 7))
print(a.subtract(2, 8))
print(a.delete(4, 9))
print(a.multiply(5, 10))