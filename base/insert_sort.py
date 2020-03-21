def inset_sort(arr):
    for i in range(len(arr)):
        current_value = arr[i]
        for j in range(i-1, -1, -1):
            compare_value=arr[j]
            if(current_value < compare_value):
                arr[j+1]=arr[j]
                arr[j]=current_value
            else:
                break

if __name__ == "__main__":
    data=[4,3,8,4,6,2,0]
    inset_sort(data)

    print(data)
