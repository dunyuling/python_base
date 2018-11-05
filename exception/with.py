class MyContext(object):
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('__enter__')
        return self

    def do_self(self):
        print('do_self')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        print('Error:',exc_type,',info:',exc_val,',traceback:',exc_tb)
        # print(exc_val,'\n\n',exc_tb)

if __name__ == '__main__':
    with MyContext('my_context') as f:
        print(f.name)
        f.do_self()
