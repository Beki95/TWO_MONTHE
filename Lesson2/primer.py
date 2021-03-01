class Complex:

    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def add(self, x2, y2, oper2="+", i="i"):
        result = f"{self.x1 + x2} {oper2} {self.y1 + y2}{i}"
        return result

    def subtract(self, x2, y2, oper="+", i="i"):
        result = f"{self.x1 - x2} {self.y1 - y2}{i}"
        if y2 < 0:
            result = f"{self.x1 - x2} {oper} {self.y1 - y2}{i}"
        return result

    def multiply(self, x2, y2, oper="+", i="i"):
        bracket1 = self.x1 * x2 - self.y1 * y2
        bracket2 = self.x1 * y2 + self.y1 * x2
        result = f"{bracket1} {oper} {bracket2}{i}"
        return result

    def delete(self, x2, y2, i="i"):
        bracket1 = self.x1 * x2 + self.y1 * y2
        bracket2 = self.y1 * x2 - self.x1 * y2
        result = f"""{bracket1}/{x2**2 + y2**2} + {bracket2}{i}/{x2**2 + y2**2}"""
        return result


a = Complex(2, 3)
print(a.add(5, 7))
print(a.subtract(5, -2))
print(a.multiply(5, -2))
print(a.delete(5, 2))