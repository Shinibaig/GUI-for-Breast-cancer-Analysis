import pandas as pd
import numpy as np
from collections import Counter
import random

def k_nearest_neighbours (data,predict,k=3):

    distances=[]
    for values in data:
        for each_val in data[values]:
            # the ecud distances
            dist=np.linalg.norm(np.array(each_val)-np.array(predict))
            distances.append([dist,values])
    votes=[i[1] for i in sorted(distances)[:k]]
    result=Counter(votes).most_common(1)[0][0]
    return result


def get_df():
    df = pd.read_csv('data.csv')
    diagnosis = df['diagnosis'].map(lambda row: 1 if row == 'M' else 0)
    df.drop(['Unnamed: 32', 'id'], inplace=True, axis=1)
    # df['diagnosis'].replace(['M','B'],[0,1], inplace=True)
    diagnosis = df['diagnosis'].map(lambda row: 1 if row == 'M' else 0)
    df.drop(['diagnosis'], inplace=True, axis=1)
    df['diagnosis'] = diagnosis
    return df
df=get_df()
print(df.head())

def getpred():
    df = get_df()
    pred = df.mean()[:-1]
    return pred

pred = getpred()
df = get_df()

df2 = df.astype(float).values.tolist()
random.shuffle(df2)
#print(df2)
# o for malignant and 1 for benign


### check



# Rechecking here
# print(len(train_set[1])+len(train_set[0]))
# print(len(train_data))



def Accuracy_Indicator(df2):
    test_size = 0.2

    train_set = {0.0: [], 1.0: []}
    test_set = {0.0: [], 1.0: []}
    train_data = df2[:-int(test_size * len(df2))]
    test_data = df2[int(test_size * len(df2)):]
    for i in train_data:
        train_set[i[-1]].append(i[:-1])
    for i in test_data:
        test_set[i[-1]].append(i[:-1])
    correct = 0
    total = 0
    votes = 0
    for group in test_set:
        for data in test_set[group]:
            votes = k_nearest_neighbours(data=train_set, predict=data, k=5)
            if group == votes:
                correct += 1
            total = total + 1
    return (correct / total)


print(Accuracy_Indicator(df2))




