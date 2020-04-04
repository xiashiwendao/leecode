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