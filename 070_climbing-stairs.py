lst = []
def f( n:int) ->int:
    global lst
    if(n<=1):
        lst.append(1)
        return 1
    
    ret = lst[n-2]+lst[n-1]
    lst.append(ret)

    return ret

import sys
if __name__ == "__main__":
    print(sys.argv[1])
    for i in range(6):
        f(i)

    print(lst)