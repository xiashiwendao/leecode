def sort(data_raw):
    size=len(data_raw)
    data=data_raw.copy()
    
    sortFlag = True
   
    for i in range(size):
        if not sortFlag:
            # print('no need to contiue')
            break
        # else:
        #     print('need to continue')

        sortFlag=False
        for j in range(size-i-1):
            if(data[j]>data[j+1]):
                temp=data[j]
                data[j]=data[j+1]
                data[j+1]=temp
                
                sortFlag=True
    return data

if __name__ == "__main__":
    data=[4,2,5,8,3,2,7]
    # data=[1,2,3,4,5]
    # data=[5,4,3,2,1]
    data_sorted=sort(data)
    print(data_sorted)
