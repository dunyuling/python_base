class Programmer(object):
    favor = 'basketball'

    def __init__(self,name,age,weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_age(self):
        return self._age

    @classmethod
    def get_favor(cls):
        return cls.favor

    @property
    def get_weight(self):
        return self.__weight

    def self_intro(self):
        print('My name is %s\nI am %s years old\n' %(self.name,self._age))

class BackendProgrammer(Programmer):
    def __init__(self,name,age,weight,language):
        super(BackendProgrammer,self).__init__(name,age,weight)
        self.language = language


if __name__ == "__main__":
    programmer = BackendProgrammer('Pro', 23, 65,'Python')
    print(dir(programmer))
    print(programmer.__dict__)
    print(type(programmer))
    print(isinstance(programmer,Programmer))
    print(issubclass(BackendProgrammer,Programmer))

