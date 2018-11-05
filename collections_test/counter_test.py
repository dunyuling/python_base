from collections import Counter

#list
"""
users = ['u1', 'u2', 'u3', 'u1', 'u4', 'u1', 'u2']
print(id(users))
user_count = Counter(users)
print(user_count)
"""

#tuple
"""
users = ('u1', 'u2', 'u3', 'u1', 'u4', 'u1', 'u2')
print(id(users))
user_count = Counter(users)
print(user_count)
"""

#dict
"""
users = {'u1':1,'u2':2,'u3':3,'u1':4}
print(id(users))
user_count = Counter(users)
print(user_count)
"""

#str
"""
user_count = Counter('aadefiissuil')
print(user_count)
"""

#update
"""
c = Counter('which')
c.update('witch')           # add elements from another iterable
d = Counter('watch')
c.update(d)                 # add elements from another counter
print(c['h'])
"""


#most_common
#top n , heap
c = Counter('abcdeabcdabcaba')
print(c.most_common(3))
print(c.most_common())
print(c.most_common(None))
