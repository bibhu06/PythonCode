import math
def divide(dividend,divisor):
    quotient = float(dividend/divisor)
    print(math.floor(quotient))

dividend = int(input("Enter the Dividend"))
divisor = int(input("Enter the Divisor"))
divide(dividend,divisor)