class Programmer(object):
    def __new__(cls, *args, **kwargs):
        print('call __new__ method')
        print(args)
        return super(Programmer,cls).__new__(cls)

    def __init__(self,name ,age):
        print('call __init__ method')
        self.name = name
        self.age = age

if __name__ == '__main__':
    programmer = Programmer('Pro',23)
    print(programmer.__dict__)
