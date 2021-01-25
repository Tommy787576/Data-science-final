## Predict Total then Guess
前處理
```cmd
python Preprocess.py input output date
```
訓練+預測總數
```cmd
python Predict_Total.py train test model total_predict
```
預測Ranking
```cmd
python Predict_Rank.py train total_predict rank_predict
```
Map24評估
```cmd
python Map24.py test rank_predict
```
Example
```cmd
python Preprocess.py train_ver2.csv 1604.csv 2016-04-28
python Preprocess.py train_ver2.csv 1605.csv 2016-05-28
python Predict_Total.py 1604.csv 1605.csv model total.csv
python Predict_Rank.py 1604.csv total.csv rank.csv
python Map24.py 1605.csv rank.csv
```
