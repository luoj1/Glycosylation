from N_rf_helper import *
import pandas as pd  
import numpy as np  
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import random

pos_dataset = pd.read_csv('./merge/intersected/processed_positive_noGO.csv',index_col = 0)  
neg_dataset = pd.read_csv('./merge/intersected/processed_negative_noGO.csv',index_col = 0)  

pos_dataset = pos_dataset.drop(columns=["ID"])
neg_dataset = neg_dataset.drop(columns=["ID"])

pos_dataset = pos_dataset.drop(columns=["site"])
neg_dataset = neg_dataset.drop(columns=["site"])

#print(pos_dataset)
#print(neg_dataset)

all_dataset_concat = pd.concat([pos_dataset,neg_dataset],sort=False)
print(all_dataset_concat)
all_dataset = [tuple([np.float32(num) for num in row[1:]]) for row in all_dataset_concat.itertuples()]
#print(all_dataset[:2])
label_pos = [np.float32(1) for _ in range(len(pos_dataset.index))] 
label_neg = [np.float32(0) for _ in range(len(neg_dataset.index))]

all_label = label_pos + label_neg

nans = np.where(np.isnan(all_dataset))
for r in set(nans[0].tolist()):
	all_dataset[r] = None
	all_label[r] = None

tmp_d = []
tmp_l = []
for i in range(len(all_dataset)):
	if not all_dataset[i] == None:
		tmp_d .append(all_dataset[i])
		tmp_l.append(all_label[i])

all_dataset = tmp_d
all_label = tmp_l

randomizer = list(zip(all_dataset,all_label))
random.shuffle(randomizer)
randomizer = list(zip(*randomizer))

all_dataset = list(randomizer[0])
print(len(all_dataset))
all_label = list(randomizer[1])
print(len(all_label))
#concat pos and neg together and produce a matrix of labeling

#may need further processing to have a bit map like matrix



data_train, data_test, label_train, label_test = train_test_split(all_dataset, all_label, test_size=0.2, random_state=0)

regressor = RandomForestRegressor(n_estimators=20, random_state=0)  
regressor.fit(data_train, label_train)  
pred = regressor.predict(data_test)  

real_pred = [1 if p > 0.5 else 0 for p in pred.tolist()]
success = 0
for i in range(len(real_pred)):
	if real_pred[i] == label_test[i]:
		success += 1
print("sucess rate", success/len(pred))
print('Mean Absolute Error:', metrics.mean_absolute_error(label_test, pred))  
print('Mean Squared Error:', metrics.mean_squared_error(label_test, pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(label_test, pred)))  