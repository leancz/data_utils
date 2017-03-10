def dict_compare(d1, d2):
    output = []
    stack = []
    stack.append(('', d1, d2))
    while len(stack)> 0:
        path, obj1, obj2 = stack.pop()
        if (type(obj1) != type({})) or (type(obj2) != type({})):
            if obj1 != obj2:
                output.append(('Value difference', path, obj1, obj2))
        else:
            if obj1.keys() != obj2.keys():
                output.append(('Key difference', path, obj1.keys(), obj2.keys()))
            else:
                for i in obj1.keys():
                    stack.append((path + '[' + str(i) + ']', obj1[i], obj2[i]))
    return output
