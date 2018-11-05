from collections import OrderedDict

user_dict = OrderedDict()
user_dict['b'] = 1
user_dict['a'] = 2 
user_dict['c'] = 3
print(user_dict)

print()
print(user_dict.move_to_end('a'))
print(user_dict)

print()
print(user_dict.pop('b'))
print(user_dict)

print()
print(user_dict.popitem(False))
print(user_dict)
