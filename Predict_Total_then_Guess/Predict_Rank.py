import pandas as pd
import sys

df = pd.read_csv(sys.argv[1])

df['total'] = df.loc[:,'ind_ahor_fin_ult1':'ind_recibo_ult1'].sum(axis = 1)
df_a = df.loc[:, ["total"]].join(df.loc[:, "ind_ahor_fin_ult1":"ind_recibo_ult1"]) 
df_a = df_a.groupby("total").agg("sum")
df_a = df_a.T

arr = []
for i in range(14):
    a = df_a[i+1]
    c1 = a.reset_index(drop=True).sort_values(ascending=False)
    arr.append('')
    for j in range(24):
        arr[i] = arr[i]+str(c1.index[j])+' '

sub = pd.read_csv(sys.argv[2])

sub['predict'] = sub['predict'].replace({0: arr[0]})
for i in range(14):
    sub['predict'] = sub['predict'].replace({i+1: arr[i]})

sub.to_csv(sys.argv[3], index=False)