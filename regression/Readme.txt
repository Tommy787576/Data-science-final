我用google colab來執行，環境可參考:
python 3.7
pytorch 1.7.0
tensorboardX 2.1 (不一定要)

內容:
/Top folder
  -/Data
    -/processed
      -train.csv (link: https://drive.google.com/file/d/17H3TnIGGDaDErWpJNy4SAYzo_u3PpyUS/view?usp=sharing)
      -dev.csv (link: https://drive.google.com/file/d/1zyVoWe3zJdu5V8XbnuhRLfxkgLwE2JFg/view?usp=sharing)
      -test.csv (link: https://drive.google.com/file/d/17AYJGPCjClu7y5Ff8YR-XIJn2656MCt1/view?usp=sharing)
      -process.docx (簡單紀錄preprocess)
  -train.ipynb (訓練logistic regression)<--可以直接用這個就好
  -process.ipynb (preprocess，內容有點亂)
  -test.ipynb (讀取訓練好的model並預測，輸出成kaggle繳交格式)
