<<<<<<< HEAD
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
=======
import numpy as np
from sklearn.decomposition import PCA, KernelPCA
import matplotlib.pyplot as plt

import math
x=[]
y=[]
N = 500
for i in range(N):
    deg = np.random.randint(0,360)
    if np.random.randint(0,2)%2==0:
        x.append([6*math.sin(deg), 6*math.cos(deg)])
        y.append(1)
    else:
        x.append([15*math.sin(deg), 15*math.cos(deg)])
        y.append(0)
y = np.array(y)
x = np.array(x)
print('ok')

kpca = KernelPCA(kernel="rbf", n_components=14)
x_kpca = kpca.fit_transform(x)

from sklearn import svm
clf = svm.SVC(kernel='linear')

clf.fit(x_kpca[:0.8*N],y[:0.8*N])
y0 = y[0.8*N:]
y1 = clf.predict(x_kpca[0.8*N:])
print(np.linalg.norm(y0-y1, 1))
>>>>>>> a70f66245562216c8453bfe2697307f3a747a707
