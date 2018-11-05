user_tuple = ('bobby', 29, 176, 'beijing', 'edu')
name, *other = user_tuple

print(name, *other)
print(name, other)

a_tuple = (1,2)
#a_tuple[0] = 3 #error

b_tuple = (1,[2,3])
b_tuple[1].append(4)

user_dict = {}
user_dict[a_tuple] = 3
#user_dict[b_tuple] = 4 #error

a_list = [1,2]
user_dict[a_list] = 5 #error
