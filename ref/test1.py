def pass_immutable_var(v):
    print('inner before id:%d, value: %d' %(id(v),v))
    v = 1000
    print('inner after id:%d, value: %d' %(id(v),v))

if __name__ == "__main__":
    v = 100
    print('before id:%d, value: %d' %(id(v),v))
    pass_immutable_var(v)
    print('after id:%d, value: %d' %(id(v),v))

