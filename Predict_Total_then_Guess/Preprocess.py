import numpy as np
import pandas as pd
import sys 

df = pd.read_csv(sys.argv[1])

# 只取一個月的資料
df = df[df["fecha_dato"] == sys.argv[3]]

# 刪掉幾乎全部都是nan的兩個column
df.drop(['ult_fec_cli_1t', 'conyuemp'], inplace=True, axis=1)

# 刪掉數值都是1.0的column
df.drop(['tipodom'], inplace=True, axis=1)

# 刪掉時間、客戶代碼
df.drop(['ncodpers', 'fecha_alta', 'fecha_dato'], inplace=True, axis=1)

# 把國家、省分代碼拿掉，換成以省分為feature，並且讓其他國家為others
df.drop(["pais_residencia", "cod_prov"], inplace=True, axis=1)
df.loc[df.nomprov.isnull(),"nomprov"] = "OTHERS"

# 刪掉幾乎都是nan的那幾筆資料
df.drop(np.where(df.iloc[:, 2].isnull())[0], inplace=True)
df.reset_index(drop=True, inplace=True)

# 避免數字前有空格的情況發生
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["antiguedad"] = pd.to_numeric(df["antiguedad"], errors="coerce")
df.drop(np.where(df.antiguedad < 0)[0], inplace=True)
df.reset_index(drop=True, inplace=True)
df["indrel_1mes"] = pd.to_numeric(df["indrel_1mes"], errors="coerce")

# 把剩下有nan的row全部刪掉
df.dropna(inplace=True)

df.to_csv(sys.argv[2], index=False)
