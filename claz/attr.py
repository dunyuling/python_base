class Programmer(object):
    favor = 'basketball'

    def __init__(self,name,age,weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_age(self):
        return self._age

    def get_weight(self):
        return self.__weight

if __name__ == '__main__':
    programmer = Programmer('Pro',23,65)
    print(dir(programmer))
    print(programmer._age)
    print(programmer.get_age())
    print(programmer.__dict__)
    print(programmer.get_weight())
    print(programmer._Programmer__weight)
    print(programmer.favor)
    print(Programmer.favor)