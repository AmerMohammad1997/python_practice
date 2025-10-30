class Calculator:
    def multiplyin(self, a=1,b=1,*args):
        result = a*b
        for num in args:
            result *= num
        return result

cals = Calculator()
print(cals.multiplyin())
print(cals.multiplyin(5,10))
print(cals.multiplyin(2, 4, 10))