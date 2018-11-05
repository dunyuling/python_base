import os

try:
    f = open("11")
    print(f.read())
    f.seek(-5,os.SEEK_SET)
except IOError as e:
    print(1,e)
except ValueError as e:
    print(2,e)
finally:
    f.close()
print(3,f.closed)

print("-----------")

try:
    with open("11") as f1:
        print(f1.read())
        f.seek(-5, os.SEEK_SET)
except IOError as e:
    print(e)
    print(f1.closed)