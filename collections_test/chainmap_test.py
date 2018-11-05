from collections import ChainMap

#no repeat key
"""
user_dict1 = {'a':'a','b':'b'}
user_dict2 = {'c':'c','d':'d'}
new_dict = ChainMap(user_dict1, user_dict2)
print(new_dict)
for key,value in new_dict.items():
    print(key, value)
"""

#has repeat key
"""
user_dict1 = {'a':'a','b':'b'}
user_dict2 = {'b':'c','d':'d'}
new_dict = ChainMap(user_dict1, user_dict2)
print(new_dict)
for key,value in new_dict.items():
    print(key, value)
"""

#new_child
"""
user_dict1 = {'a':'a','b':'b'}
user_dict2 = {'c':'c','d':'d'}
new_dict = ChainMap(user_dict1, user_dict2)
print(id(new_dict),new_dict)
print([x for x in new_dict.items()])
print()
new_dict = new_dict.new_child({'e':'e', 'f':'f'})
print(id(new_dict),new_dict)
print([x for x in new_dict.items()])
for key,value in new_dict.items():
    print(key, value)
"""

#maps
user_dict1 = {'a':'a','b':'b'}
user_dict2 = {'c':'c','d':'d'}
new_dict = ChainMap(user_dict1, user_dict2)
print(id(user_dict1))
print(id(new_dict.maps[0]))
