import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

df = pd.read_csv('dataset\\Iris.csv')
X = df.values[:, 0:4].astype(float)
Y = df.values[:, 4]

labelEncoder = LabelEncoder()
Y_encoder = labelEncoder.fit_transform(Y)
Y_onehot = np_utils.to_categorical(Y_encoder)

def baseline_model():
    model = Sequential()
    model.add(Dense(7, input_dim=4, activation='tanh'))
    model.add(Dense(4, activation='softmax'))
    model.compile(loss='means_square_error', optimizer='sgd', metrics=['accuracy'])

    return model

kfold = KFold(n_split=10, shuffle=True, random_state=seed)
estimator=KerasClassifier(build_fn=baseline_model, epochs=20, batch_size=1, verbose=1)
result = cross_val_score(estimator, X, Y_onehot, cv=10)
print('cv mean: %s, sd: %s'%(result.mean(), result.std()))

# estimator.fit(X, Y_onehot)
