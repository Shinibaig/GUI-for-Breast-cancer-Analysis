import pandas as pd
import numpy as np
from collections import Counter
import random # to shuffle dataset

def k_nearest_neighbours(data,predict,k=3)  :

    if k>=len(data[1]):
        print("Warning, k> then the data set")
    distance=[]
    # iterates through each row
    for row in data:
        for features in data[row]:
            #this finds the distance between our data and each value in dataset
            act_dist=np.linalg.norm(np.array(features)-np.array(predict))
            distance.append([act_dist,row])
    # finds the top k distances
    classes=[i[1] for i in sorted(distance)[:k]]
    #The most common group and how many there were near to it
    results=Counter(classes).most_common(1)[0][0]
    return results

##########################################################################
#################### MAIN PROGRAM #######################################
# data cleaning and allocation
df = pd.read_csv('data.csv')
df.drop(['Unnamed: 32','id'],inplace=True,axis=1)
#  Change the diagonisis from string to Float to make them easier to manipulate
diagnosis=df['diagnosis'].map(lambda row:1 if row=='M' else 0)
df.drop(['diagnosis'],inplace=True,axis=1)
df['diagnosis']=diagnosis
#print(df)
# print(df.isnull().sum()) # very clean dataset
# reading all the columns names in the data

# convert to 2d array by rows
df2=df.astype(float).values.tolist()
random.shuffle(df2)

### Training and Testing our data

# we seperate the malignant and begin values into 2 categories
train_size=0.3
test_set={1:[],0:[]}
train_set={1:[],0:[]}
train_data=df2[:-int(len(df2)*train_size)]
test_data=df2[int(len(df2)*train_size):]
for i in train_data:
    train_set[i[-1]].append(i[:-1])
for i in test_data:
    test_set[i[-1]].append(i[:-1])

# Rechecking here
# print(len(train_set[1])+len(train_set[0]))
# print(len(train_data))

# Rechecking our code
correct=0
total=0
vote=0
for group in test_set:
    for data in test_set[group]:
        votes=k_nearest_neighbours(data=train_set,predict=data,k=5)
        if group==vote:
            correct+=1
        total+=1
print(correct/total)


########### WHOLE CODE WITH HIGH ACCURACY
# import pandas as pd
# import numpy as np
# from collections import Counter
# import random
#
# def k_nearest_neighbours (data,predict,k=3):
#
#     distances=[]
#     for values in data:
#         for each_val in data[values]:
#             # the ecud distances
#             dist=np.linalg.norm(np.array(each_val)-np.array(predict))
#             distances.append([dist,values])
#     votes=[i[1] for i in sorted(distances)[:k]]
#     result=Counter(votes).most_common(1)[0][0]
#     return result
#
#
# df=pd.read_csv('data.csv')
# diagnosis=df['diagnosis'].map(lambda row:1 if row=='M' else 0)
# df.drop(['Unnamed: 32','id'],inplace=True,axis=1)
# print(df)
# df2=df.astype(float).values.tolist()
# random.shuffle(df2)
# print(df2)
#
# test_size=0.2
# train_set={2:[],4:[]}
# test_set={2:[],4:[]}
# train_data=df2[:-int(test_size*len(df2))]
# test_data=df2[int(test_size*len(df2)):]
#
# for i in train_data:
#     train_set[i[-1]].append(i[:-1])
# for i in test_data:
#     test_set[i[-1]].append(i[:-1])
#
#
#
#
# def Accuracy_Indicator(test_set,train_set):
#     correct = 0
#     total = 0
#     votes = 0
#     for group in test_set:
#         for data in test_set[group]:
#             votes = k_nearest_neighbours(data=train_set, predict=data, k=5)
#             if group == votes:
#                 correct += 1
#             total = total + 1
#     return (correct / total)
#
#
# print(Accuracy_Indicator(test_set,train_set))












