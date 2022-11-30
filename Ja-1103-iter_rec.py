'''
The function iterativePower has base and exponential
    if the base is the power of 0 
        it is going to be equal to 1
    else the base is going to multiply itself with the amount of exponent
print iterativePower contain base 3 and exponent 1

'''

def iterativePower(base, exp):
    if exp == 0:
        return 1
    else:
        OriginalBase = base
        for i in range (exp - 1):
            base = OriginalBase
        return base

print(iterativePower(3,1))

'''
The function iterativePower has base and exponential
    if the base is the power of 0 
        it is going to equal to 1
    else multiply the result with the base
print recursivePower contain base 3 and exponent 1

'''

def recursivePower(base, exp):
    if exp == 0:
        return 1
    else:
        return base * (recursivePower(base, exp - 1))

print(recursivePower(3,1))