import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

df1 = pd.read_csv(sys.argv[1])
df2 = pd.read_csv(sys.argv[2])

df = pd.concat([df1[:10000],df2])

# 只有兩種值改為0,1
df.loc[:,'sexo'].replace({'V' : 0, 'H' : 1}, inplace = True)
df.loc[:,'indrel'].replace({1 : 0, 99 : 1}, inplace = True)
df.loc[:,'indrel_1mes'].replace({1 : 0, 3 : 1}, inplace = True)
df.loc[:,'indresi'].replace({'N' : 0, 'S' : 1}, inplace = True)
df.loc[:,'indext'].replace({'N' : 0, 'S' : 1}, inplace = True)
df.loc[:,'indfall'].replace({'N' : 0, 'S' : 1}, inplace = True)

# 三種值以上作OHE
df = pd.get_dummies(df, columns=['ind_empleado', 'tiprel_1mes','canal_entrada','nomprov','segmento'])

# 計算商品總數
df['total'] = df.loc[:,'ind_ahor_fin_ult1':'ind_recibo_ult1'].sum(axis = 1)
a = int(np.where(df.columns == 'ind_ahor_fin_ult1')[0])
x = np.array(range(a,a+24))
df.drop(df.columns[x], inplace=True, axis=1)

# training
a = df[:10000].values
X = a[:,:-1]
y = np.reshape(a[:,-1],-1)
clf = RandomForestClassifier(random_state=0).fit(X, y)

# save model
import pickle
with open(sys.argv[3], 'wb') as f:
    pickle.dump(clf, f)

# testing
a = df[10000:].values
X_test = a[:,:-1]
y_test = np.reshape(a[:,-1],-1)
predict = clf.predict(X_test)
pre = pd.DataFrame(np.transpose(np.vstack([range(len(predict)),predict])),columns=['id', 'predict'])
pre.to_csv(sys.argv[4], index=False)

# plot importance
imp = clf.feature_importances_
a = np.array(df.columns)
plt.figure(figsize=(16,4))
plt.bar(a[np.argsort(-imp)[:20]],-np.sort(-imp)[:20])
plt.xticks(rotation=60)
plt.show()