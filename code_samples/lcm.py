
#def lcm(arg1, arg2):
    #mx = i = max(arg1, arg2)
    #mn = min(arg1, arg2)
    #while i < (arg1 * arg2):
        #if i % mn == 0:
            #return i
        #i += mx
    #return(arg1 * arg2)

def lcm(arg1, arg2):
    i = max(arg1, arg2)
    while i < (arg1 * arg2):
        if i % min(arg1, arg2) == 0:
            return i
        i += max(arg1, arg2)
    return(arg1 * arg2)

lcm(21498497, 3890120)
