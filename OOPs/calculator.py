#create a calculator Class
# do sin, cos operation
# sqrt operation, 
# Take integer and convert to binary
# Take integer and convert to hexadecimal
# hexadecimal to binary

import math

class SimpleCalculator:
    def sin_operation(self, number):
        return math.sin(number)
    
    def cos_operation(self, number):
        return math.cos(number)

    def sqrt(self, number):
        return math.sqrt(number)

    def int_to_binary(self, number):
        return bin(number)
    
    def int_to_hexa(self, number):
        return hex(number)

    def hexa_to_bin(self, hexa_num):
        return bin(hexa_num)



calc = SimpleCalculator()

print(calc.sin_operation(2))
print(calc.cos_operation(2))
print(calc.sqrt(16))
print(calc.int_to_binary(10))
print(calc.int_to_hexa(10))
print(calc.hexa_to_bin(10))

