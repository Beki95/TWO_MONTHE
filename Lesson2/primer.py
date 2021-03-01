class Complex:

    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def __add__(self, other, i="i", oper="+"):
        result = f"{self.x1 + other.x1} {oper} {self.y1 + other.y1}{i}"
        if other.y1 < 0:
            result = f"{self.x1 + other.x1} {self.y1 + other.y1}{i}"
        return result

    def __sub__(self, other, oper="+", i="i"):
        result = f"{self.x1 - other.x1} {self.y1 - other.y1}{i}"
        if other.y1 < 0:
            result = f"{self.x1 - other.x1} {oper} {self.y1 - other.y1}{i}"
        return result

    def __mul__(self, other, oper="+", i="i"):
        bracket1 = self.x1 * other.x1 - self.y1 * other.y1
        bracket2 = self.x1 * other.y1 + self.y1 * other.x1
        result = f"{bracket1} {oper} {bracket2}{i}"
        return result

    def __floordiv__(self, other, i="i"):
        bracket1 = self.x1 * other.x1 + self.y1 * other.y1
        bracket2 = self.y1 * other.x1 - self.x1 * other.y1
        denominator = other.x1 ** 2 + other.y1 ** 2
        result = f"""{bracket1}/{denominator} + {bracket2}{i}/{denominator}"""
        return result


a = Complex(2, -3)
b = Complex(5, 7)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
