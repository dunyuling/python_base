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

if __name__ == "__main__":
    programmer = Programmer('Pro', 23, 65)
    print(programmer)
    print(dir(programmer))
    print()
    print(programmer.get_favor())
    print(Programmer.get_favor())
    print()
    print(programmer.get_weight)
    print(Programmer.get_weight)
    print()
    programmer.self_intro()
    # Programmer.self_intro()
