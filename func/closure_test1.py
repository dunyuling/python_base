
def set_passline(passline):
    print('1 passline value:%d,addr:%x' % (passline, id(passline)))
    def cmp(val):
        print('2 passline value:%d, addr:%x' % (passline, id(passline)))
        print('3 val value:%d, addr:%x' %(val, id(val))) 
        if val >= passline:
            print('%d base on %d pass ' %(val, passline))
        else:
            print('%d base on %d failed ' %(val, passline))
    return cmp

f_100 = set_passline(60)
print(type(f_100), hex(id(f_100)), f_100.__closure__)
#print('%x: ' % id(f_100))
f_100(89)
print()
f_150 = set_passline(90)
print(type(f_150), hex(id(f_150)), f_150.__closure__)
f_150(89)
