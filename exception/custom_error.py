#!/usr/bin/python
class CustomError(Exception):
    def __init__(self,info):
        Exception.__init__(self)
        self.error_info  = info
        print(id(self))

    def __str__(self):
        return 'CustomError:%s' % self.error_info

if __name__ == '__main__':
    try:
        raise CustomError("my custom error")
    except CustomError as e:
        print(id(e),e)
