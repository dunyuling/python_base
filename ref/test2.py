def pass_obj_ref(v):
    print('inner before id:%d, value: %s' %(id(v),v))
    v.append(999)
    print('inner after id:%d, value: %s' %(id(v),v))

if __name__ == "__main__":
    v = ['100']
    print('before id:%d, value: %s' %(id(v),v))
    pass_obj_ref(v)
    print('after id:%d, value: %s' %(id(v),v))
