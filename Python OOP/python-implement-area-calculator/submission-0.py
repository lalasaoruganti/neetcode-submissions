import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width=None):
        if not width:
            p = math.pi
            area = p * length ** 2
            res = round(area,2)
            return res
        else:
            area = length * width
            return area

    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
