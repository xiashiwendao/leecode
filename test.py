one_bit_center = [0, 1, 8]
two_bit_center = [11, 69, 88, 96]
def center_rec(n, data):
    if(n > 2):
        center_rec(n-2, data)
    if(len(data)==0):
        if(n==1):
            data = one_bit_center
        elif(n==2):
            data = two_bit_center
        else:
            print('error: data length is 0')
    ret = []
    for d in data:
        for item in two_bit_center:
            value = str(item)[0]+str(d)+str(item)[1]
            ret.append(value)

    return ret

def center_entry(n, data):
    
    if(n == 0):
        return []
    if(n == 1):
        return one_bit_center
    if(n==2):
        return two_bit_center

    data = center_entry(n-2, data)
    
    ret = []
    for d in data:
        for item in two_bit_center:
            value = str(item)[0]+str(d)+str(item)[1]
            ret.append(value)

    return ret

if __name__ == "__main__":
    ret = center_entry(5, [])
    print(ret)