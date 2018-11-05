"""
class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User(name='bobby', age=29)
print(user.name, user.age)
"""

"""
运行观察效果,描述起来较复杂,故此省略
def ask(*args, **kwargs):
    print(0, *args, kwargs)
    print(1, *args, *kwargs)
    print(2, *args, **kwargs)
    print(3, args, kwargs)
    print(4, args, *kwargs)
    print(5, args, **kwargs)

ask('bobby', 29) 
print()
ask(name='bobby', age=29)
"""

from collections import namedtuple

User = namedtuple('User', ['name', 'age', 'height', 'edu'])
#0
#user = User(name='bobby', age=29, height=175, edu='master')

#1
#user_tuple = ('bobby', 29, 175)
#user = User(*user_tuple, 'master')
#print(user_tuple)
#print(*user_tuple)

#2
#user_dict = {
#    'name':'bobby',
#    'age':29,
#    'height':175
#}
#user = User(*user_dict, edu='master')
#print(user.name, user.age, user.height, user.edu)
#user = User(**user_dict, edu='master')
#print(user.name, user.age, user.height, user.edu)

#3
#user_tuple = ('bobby', 29, 175, 'master')
#user = User._make(user_tuple)
#user_list = ['bobby', 29, 175, 'master']
#user = User._make(user_list)
user_dict = {
    'name':'bobby',
    'age':29,
    'height':175,
    'edu':'master'
}
user = User._make(user_dict) 
print(user.name, user.age, user.height, user.edu) #can not get right dict
user_info = user._asdict()
print(user_info)
