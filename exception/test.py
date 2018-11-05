a = 3
try:
    1/0
except IOError as e:
    print("aa")
except NameError as e:
    print("bb")
else:
    print("dd")
finally:
    print("cc")
