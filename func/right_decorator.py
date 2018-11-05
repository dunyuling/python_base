def deco(func):
    def in_deco():
        print('in deco')
        func()
    print('call deco')
    return in_deco

@deco
def bar():
    print('in bar')

print(type(bar))
bar()
