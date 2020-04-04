one_bit_center = [0, 1, 8]
two_bit_center = [11, 69, 88, 96]
def center_entry(n, m, data):
    if(n == 0):
        return []
    if(n == 1):
        return one_bit_center
    if(n==2):
        return two_bit_center

    data = center_entry(n-2, m, data)
    
    ret = []
    for d in data:
        if n != m:
            value = "0"+str(d)+"0"
            ret.append(value)
        for item in two_bit_center:
            value = str(item)[0]+str(d)+str(item)[1]
            ret.append(value)

    return ret

if __name__ == "__main__":
    ret = center_entry(5, 5, [])
    print(ret)