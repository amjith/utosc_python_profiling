import sys
import operator as op

@profile
def compute(*args):
    op_s = args[0]
    nums = map(int, args[1:])
    if op_s == "power":
        result = reduce(op.pow, nums)
    elif op_s == "plus":
        result = reduce(op.add, nums)
    elif op_s == "product":
        result = reduce(op.mul, nums)
    elif op_s == "minus":
        result = reduce(op.sub, nums)
    elif op_s == "div":
        result = reduce(op.div, nums)
    elif op_s == "sumsquare":
        result = reduce(lambda x, y: x**2 + y**2, nums)
    return result


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        for line in f:
            compute(*line.split())
