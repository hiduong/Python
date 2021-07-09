
from functools import reduce

def function(L):
    temp = map(lambda x: (x.count('*'),x)L)
    result = reduce((lambda x, y: x if x[0] > y[0] else y), temp)
    return result[1]

def function2(x):
    pass

def function3(x):
    pass


if __name__ == "__main__":
    function(input())