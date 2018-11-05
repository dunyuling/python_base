#not closure, code repeated 
"""
def my_sum(*arg):
    if len(arg) == 0:
        return 0
    for val in arg:
        if not isinstance(val, int):
            return 0
    return sum(arg)

def my_average(*arg):
    if len(arg) == 0:
        return 0
    for val in arg:
        if not isinstance(val, int):
            return 0
    return sum(arg)/len(arg)

print(my_sum(1, 2, 3, 4, 5))
print(my_sum(1, 2, 3, 4, 5, '6'))
print(my_average(1, 2, 3, 4, 5))
print(my_average())
"""

#with closure, code concise
def my_sum(*arg):
    return sum(arg)

def my_average(*arg):
    return sum(arg)/len(arg)

def dec(func):
    def in_dec(*arg):
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val, int):
                return 0
        #print('func id: ', hex(id(func)))
        return func(*arg)
    #print('in_dec id: ',hex(id(in_dec)))
    return in_dec
        
#print('original my_sum id: ', hex(id(my_sum)))
my_sum = dec(my_sum)
#print(hex(id(my_sum)))
print(my_sum(1, 2, 3, 4, 5))
print(my_sum(1, 2, 3, 4, 5, '6'))
print()
my_average = dec(my_average)
print(my_average(1, 2, 3, 4, 5))
print(my_average())
