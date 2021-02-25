class Fraction:

    def __init__(self, fraction):
        self.fraction = fraction

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

    def prosto(self, f, fraction1):
        ret = None
        ret1 = None
        if f[0] == fraction1[1]:
            f[0], fraction1[1] = 1, 1
        else:
            ret1 = self.dont_num(f[0], fraction1[1])
        if f[1] == fraction1[0]:
            f[1], fraction1[0] = 1, 1
        else:
            ret = self.dont_num(f[1], fraction1[0])
        if ret is None:
            pass
        else:
            fraction1[0] //= ret
            f[1] //= ret
        if ret1 is None:
            pass
        else:
            f[0] //= ret1
            fraction1[1] //= ret1
        result = f[0] * fraction1[0], f[1] * fraction1[1]
        return result

    def add(self, f):
        if self.fraction[1] == f[1]:
            num = self.fraction[0] + f[0]
            return num, f[1]
        else:
            m = self.fraction[1]
            res = self.dont_znam(m, f[1])

            result_first = self.fraction[0] * res[0] + f[0] * res[1]
            return result_first, res[2]

    def subtract(self, f):
        if self.fraction[1] == f[1]:
            num = self.fraction[0] - f[0]
            return num, f[1]
        else:
            m = self.fraction[1]
            res = self.dont_znam(m, f[1])
            result_first = self.fraction[0] * res[0] - f[0] * res[1]
            return result_first, res[2]

    def delete(self, f):
        fraction1 = list(self.fraction)
        f = list(f)
        f[0], f[1] = f[1], f[0]
        return self.prosto(f, fraction1)

    def multiply(self, f):
        fraction1 = list(self.fraction)
        f = list(f)
        return self.prosto(f, fraction1)


a = Fraction((2, 6))

print(a.add((2, 7)))
print(a.subtract((2, 8)))
print(a.delete((4, 9)))
print(a.multiply((5, 10)))
