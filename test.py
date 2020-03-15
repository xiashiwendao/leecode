import datetime


def datetime_operate(n:int):
    now = datetime.datetime.now()  # 获取当前时间
    _new_date = now + datetime.timedelta(days=n)  # 获取指定天数后的新日期
    new_date = _new_date.strftime("%Y%m%d")  # 转换为指定的输出格式
    return new_date

from matplotlib import pyplot as plt
import math
def drawEntropy():
    x = list(range(1, 100, 1))
    x = [item/100 for item in x]
    y=[]
    for item in x:
        entropy = math.log2(item)
        print('+++++ entropy: ', entropy, ', item: ', item)
        y_temp = item*entropy
        y.append(y_temp)
    plt.plot(x, y)
    plt.show()
import json
def dictToJson():
    dic={1:"B", 2:"A"}
    s=json.dumps(dic)
    print('json: ', s)
    dic_2=json.loads(s)
    print('dict: ', dic_2)
import numpy as np
if __name__ == '__main__':
    # print(datetime_operate(4))
    # drawEntropy()
    # dictToJson()
    # for i in range(6, -1,-1):
    #     print(i)
    # a = 'Φ'
    # b = 'Φ'
    # if a is b:
    #     print('a is b !')
    # else:
    #     print('they are not the same')
    # ar=np.array([2,3,4,5])
    # print(ar[0:0])
    # from string import ascii_lowercase
    # s = 'alablba'
    # b = ['a','b','c','d','e','f']
    # for index, item in enumerate(b):
    #     print(index, item)
    for i in range(6, 10):
        print(i)
