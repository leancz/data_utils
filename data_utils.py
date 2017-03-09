def dict_compare(d1, d2):
    stack = []
    stack.append(('', d1, d2))
    while len(stack)> 0:
        path, obj1, obj2 = stack.pop()
        if type(obj1) != type({}):
            if obj1 != obj2:
                print('Value difference at {}: {} != {}'.format(path, obj1, obj2))
        else:
            if obj1.keys() != obj2.keys():
                print('Key difference at {}: {} != {}'.format(path, obj1.keys(), obj2.keys()))
            else:
                for i in obj1.keys():
                    stack.append((path + '[' + str(i) + ']', obj1[i], obj2[i]))
                    
