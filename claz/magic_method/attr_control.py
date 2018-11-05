class Programmer(object):

    def __init__(self,name,age):
        self.name = name
        self._age = age

    def __getattribute__(self, name):
        # return getattr(self,name)
        # return self.__dict__[name]
        return super(Programmer,self).__getattribute__(name)
        # return {'a':1}
        # return {1:1}


    def __setattr__(self, name, value):
        # setattr(self,name,value)
        self.__dict__[name] = value

if __name__ == '__main__':
    p = Programmer('Pro',23)
    print(p.name)
    delattr(p,'name')
    print(dir(p))
    # print(p.name)