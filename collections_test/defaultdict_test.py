"""
user_dict = {}
users = ['u1', 'u2', 'u3', 'u1', 'u2', 'u1']
for user in users:
    if user not in user_dict:
        user_dict[user] = 1
    else: 
        user_dict[user] += 1

print(user_dict)
"""

"""
user_dict = {}
users = ['u1', 'u2', 'u3', 'u1', 'u2', 'u1']
for user in users:
    user_dict.setdefault(user, 0)
    user_dict[user] += 1

print(user_dict)
"""

"""
from collections import defaultdict

user_dict = defaultdict(int) 
users = ['u1', 'u2', 'u3', 'u1', 'u2', 'u1']
for user in users:
    user_dict[user] += 1 

print(user_dict)
print(user_dict.keys())
print(user_dict.values())
"""

from collections import defaultdict

def gen_default():
    return {
        'name':'',
        'nums':0
    }

user_dict = defaultdict(gen_default) 
user_dict['group1'] 
user_dict['group2'] 
print(user_dict)
