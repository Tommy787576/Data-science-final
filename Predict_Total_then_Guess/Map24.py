import numpy as np
import pandas as pd
import sys

#pred:numpy aray(1*24), 各產品購買的機率; label:list(1*24)numpy aray, 產品label(有買=1, 沒買=0)
def map24(pred, label): 
  ind = []
  for i in range(0, len(label)): #length should be 24
    if label[i] == 1:
      ind.append(i)
  L = len(ind)
  L = min(24, L)
  if L == 0:
    return 0
  score = 0
  precision = 0
  for i in range(0, 24):
    if (pred[i] in ind):
      precision += 1
      score += precision / (i+1)
  score  = score / L
  return score

def map24all(a, b):
    temp = 0
    for i in range(len(a)):
        temp += map24(a[i], b[i])
    return temp/len(a)
df2 = pd.read_csv(sys.argv[1])
label = df2.loc[:,'ind_ahor_fin_ult1':'ind_recibo_ult1'].values

df = pd.read_csv(sys.argv[2])

predict = []
for i in range(len(df)):
    string = df.iloc[i,1].split()
    predict.append(np.array(string, dtype = np.int8))
predict = np.array(predict)

print("Map24 score: {}".format(map24all(predict,label)))