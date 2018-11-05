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

    def self_intro(self):
        print('My name is %s\nMy favorite language is %s\n' %(self.name,self.language))

def introduce(programmer):
    if isinstance(programmer,Programmer):
        programmer.self_intro()

if __name__ == "__main__":
    programmer = Programmer('Pro', 23, 65)
    p_programmer = BackendProgrammer('pPro',24,66,'Python')
    j_programmer = BackendProgrammer('jPro',25,67,'Java')

    introduce(programmer)
    print()
    introduce(p_programmer)
    print()
    introduce(j_programmer)




