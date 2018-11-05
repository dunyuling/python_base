from collections import deque
import copy

#deque GIL 线程安全, list非线程安全
#appendleft
"""
user_deque = deque(('u1', 'u2', 'u3'))
user_deque.appendleft('u0')
print(user_deque)
"""


#shallow copy 1
"""
user_deque = deque(('u1', 'u2' ,'u3'))
user_deque2 = user_deque.copy()
user_deque2[0] = 'u0' #open or close to compare

print('user_deque', id(user_deque))
print([id(x) for x in user_deque])
print(user_deque)

print('user_deque2', id(user_deque2))
print([id(x) for x in user_deque2])
print(user_deque2)
"""


#shallow copy 2
"""
user_deque = deque(('u1', ['u2' ,'u3'] ,'u4'))
user_deque2 = user_deque.copy()
user_deque2[1].append('u0') #open or close to compare  

print('user_deque', id(user_deque))
print([id(x) for x in user_deque])
print(user_deque)

print('user_deque2', id(user_deque2))
print([id(x) for x in user_deque2])
print(user_deque2)
"""


#deep copy 1
"""
user_deque = deque(('u1', 'u2' ,'u3'))
user_deque2 = copy.deepcopy(user_deque) 
user_deque2[0] = 'u0' #open or close to compare

print('user_deque', id(user_deque))
print([id(x) for x in user_deque])
print(user_deque)

print('user_deque2', id(user_deque2))
print([id(x) for x in user_deque2])
print(user_deque2)
"""


#deep copy 2
"""
user_deque = deque(('u1', ['u2' ,'u3'] ,'u4'))
user_deque2 = copy.deepcopy(user_deque) 
user_deque2[1].append('u0') #open or close to compare  

print('user_deque', id(user_deque))
print([id(x) for x in user_deque])
print(user_deque)

print('user_deque2', id(user_deque2))
print([id(x) for x in user_deque2])
print(user_deque2)
"""


#extend
"""
user_deque = deque(('u1', 'u2' ,'u3'))
print(id(user_deque))
user_deque2 = deque(('u4', 'u5' ,'u6'))
user_deque3 = user_deque.extend(user_deque2)

print(user_deque, user_deque2, user_deque3)
print(id(user_deque))
"""


#insert
"""
user_deque = deque(('u1', 'u2' ,'u3'))
user_deque.insert(0, 'u0')
print(user_deque) 
"""


#remove
"""
user_deque = deque(('u1','u1','u2'))
print([id(x) for x in user_deque])
user_deque.remove('u1')
print([id(x) for x in user_deque])
print(user_deque)
"""

#reverse
user_deque = deque(('u1', 'u2', 'u3'))
print([id(x) for x in user_deque], id(user_deque))
user_deque.reverse()
print([id(x) for x in user_deque], id(user_deque))
