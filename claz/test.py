class OldStyle:

    def __init__(self,name,desc):
        self.name = name
        self.desc = desc

class NewStyle(object):

    def __init__(self,name,desc):
        self.name = name
        self.desc = desc

if __name__ == '__main__':
    old = OldStyle('old','old style class')
    print(old)
    print(type(old))
    print(dir(old))
    print()
    new = NewStyle('new','new style class')
    print(new)
    print(type(new))
    print(dir(new))