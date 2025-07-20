```
PS D:\myProjects\hate-tweet-classifier> D:/myProjects/hate-tweet-classifier/.venv/Scripts/python.exe scripts/load_and_inspect.py
Before cleaning:
0     @user when a father is dysfunctional and is s...
1    @user @user thanks for #lyft credit i can't us...
2                                  bihday your majesty
3    #model   i love u take with u all the time in ...
4               factsguide: society now    #motivation
Name: tweet, dtype: object

After cleaning:
0    when a father is dysfunctional and is so selfi...
1    thanks for lyft credit i cant use cause they d...
2                                  bihday your majesty
3        model i love u take with u all the time in ur
4                    factsguide society now motivation
Name: clean_tweet, dtype: object

Class distribution:
label
0    29720
1     2242
Name: count, dtype: int64

Classification Report (Bag-of-Words + Logistic Regression):
              precision    recall  f1-score   support

    Harmless       0.96      0.99      0.98      5945
        Hate       0.85      0.52      0.64       448

    accuracy                           0.96      6393
   macro avg       0.91      0.76      0.81      6393
weighted avg       0.96      0.96      0.96      6393

Accuracy: 0.9597997810104802
```
