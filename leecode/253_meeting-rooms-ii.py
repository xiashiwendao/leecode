import numpy as np


def meetingroot(time_list):
    lst_timeChain = []

    for timenode in time_list:
        insert_flag = False
        for item_list in lst_timeChain:
            for i, item in enumerate(item_list):
                start = timenode[0]
                end = timenode[1]
                start_1 = item[0]
                end_1 = item[1]
                if(len(item_list) >= i+2):
                    start_2 = item_list[i+1]
                    end_2 = item_list[i+1]

                    if end_1 < start and end < start_2:
                        item_list.insert(i, timenode)
                        insert_flag = True
                else:
                    if end_1 < start:
                        item_list.append(timenode)
                        insert_flag = True

        if not insert_flag:
            lst_timenode = [timenode]
            lst_timeChain.append(lst_timenode)

    return len(lst_timeChain)


if __name__ == "__main__":
    # lst = [[0, 30],[5, 10],[15, 20]]
    lst = [[7, 10], [2, 4]]
    lst = sorted(lst, key=lambda x: x[0])
    # lst.sort(key=lambad x:x[0])
    print('sorted list: ', lst)
    room_size = meetingroot(lst)
    print('room_size: ', room_size)
