@profile
def ver_1(arg1, arg2):
    i = max(arg1, arg2)
    while i < (arg1 * arg2):
        if i % min(arg1,arg2) == 0:
            return i
        i += max(arg1,arg2)
    return(arg1 * arg2)

@profile
def ver_2(arg1, arg2):
    mx = max(arg1, arg2)
    mn = min(arg1, arg2)
    i = mx
    while i < (arg1 * arg2):
        if i % mn == 0:
            return i
        i += mx
    return(arg1 * arg2)

@profile
def ver_3(arg1, arg2):
    mx = max(arg1, arg2)
    mn = min(arg1, arg2)
    i = mx
    mx_limit = arg1*arg2
    while i < mx_limit:
        if i % mn == 0:
            return i
        i += mx
    return mx_limit


ver_1(1232005, 2001)
ver_2(1232005, 2001)
ver_3(1232005, 2001)
