from N_rf_helper import *
import pandas as pd  
import numpy as np  
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
import random
import matplotlib.pyplot as plt
import re
#pos_dataset = pd.read_csv('./merge/intersected/processed_positive2_matrix.csv',index_col = 0)  
#neg_dataset = pd.read_csv('./merge/intersected/processed_negative2_matrix.csv',index_col = 0)  
def train(pos_addr, neg_addr, seqOnly = False, resulttag = str(int(time.time()))):
	pos_dataset = pd.read_csv(pos_addr,index_col = 0)  
	neg_dataset = pd.read_csv(neg_addr,index_col = 0)  

	pos_dataset = pos_dataset.drop(columns=["ID"])
	neg_dataset = neg_dataset.drop(columns=["ID"])
	pos_dataset = pos_dataset.drop(columns=["id"])
	neg_dataset = neg_dataset.drop(columns=["id"])
	pos_dataset = pos_dataset.drop(columns=["site"])
	neg_dataset = neg_dataset.drop(columns=["site"])
	pos_dataset = pos_dataset.drop(columns=["n"])
	neg_dataset = neg_dataset.drop(columns=["n"])
	pos_dataset = pos_dataset.drop(columns=["type"])
	neg_dataset = neg_dataset.drop(columns=["type"])
	pos_dataset = pos_dataset.drop(columns=["label"])
	neg_dataset = neg_dataset.drop(columns=["label"])
	pos_dataset = pos_dataset.drop(columns=["seq"])
	neg_dataset = neg_dataset.drop(columns=["seq"])
	pos_dataset = pos_dataset.drop(columns=["q3"])
	neg_dataset = neg_dataset.drop(columns=["q3"])
	pos_dataset = pos_dataset.drop(columns=["q8"])
	neg_dataset = neg_dataset.drop(columns=["q8"])
	pos_dataset = pos_dataset.drop(columns=["disorder"])
	neg_dataset = neg_dataset.drop(columns=["disorder"])
	headers = list(neg_dataset)
	cp = []
	if seqOnly:
		for h in headers:
			if not bool(re.compile("seq?_?").match(h)) and not bool(re.compile("seq??_?").match(h)):
				cp.append(h)
		pos_dataset = pos_dataset.drop(columns=cp)
		neg_dataset = neg_dataset.drop(columns=cp)
	print(list(neg_dataset))

	#print(pos_dataset)
	#print(neg_dataset)

	all_dataset_concat = pd.concat([pos_dataset,neg_dataset],sort=False)
	#print(all_dataset_concat)
	all_dataset = [row[1:] for row in all_dataset_concat.itertuples()]

	#print(all_dataset[:2])
	label_pos = [np.float32(1) for _ in range(len(pos_dataset.index))] 
	label_neg = [np.float32(0) for _ in range(len(neg_dataset.index))]

	all_label = label_pos + label_neg
	'''
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
	'''
	randomizer = list(zip(all_dataset,all_label))
	random.shuffle(randomizer)
	randomizer = list(zip(*randomizer))
	#print(randomizer)
	all_dataset = list(randomizer[0])
	#print(len(all_dataset))
	all_label = list(randomizer[1])
	#print(len(all_label))
	#concat pos and neg together and produce a matrix of labeling

	#may need further processing to have a bit map like matrix

	data_train, data_test, label_train, label_test = train_test_split(all_dataset, all_label, test_size=0.2, random_state=0)

	regressor = RandomForestRegressor(n_estimators=20, random_state=0)  
	regressor.fit(data_train, label_train)  
	pred = regressor.predict(data_test)  
	print(len(pred.tolist()))
	print(len(label_test))


	real_pred = [1 if p > 0.5 else 0 for p in pred.tolist()]

	fpr, tpr, thresholds = metrics.roc_curve(np.array(label_test), pred)

	print('fpr: ', fpr)
	print('tpr: ', tpr)
	#plt.title('chendi_Net ROC')
	#plt.ylabel('tpr')
	#plt.xlabel('fpr')
	plt.plot(fpr, tpr,label = resulttag)
	#plt.plot([0,1], [0,1])

	success = 0
	for i in range(len(real_pred)):
		if real_pred[i] == label_test[i]:
			success += 1
	res = "sucess rate "+ str(success/len(pred)) + '\n'
	res += 'Mean Absolute Error:'+ str(metrics.mean_absolute_error(label_test, pred)) + '\n'
	res += 'Mean Squared Error:' + str(metrics.mean_squared_error(label_test, pred)) + '\n'
	res +=  'Root Mean Squared Error:' + str(np.sqrt(metrics.mean_squared_error(label_test, pred)))
	print("sucess rate", success/len(pred))
	print('Mean Absolute Error:', metrics.mean_absolute_error(label_test, pred))  
	print('Mean Squared Error:', metrics.mean_squared_error(label_test, pred))  
	print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(label_test, pred)))  


	importances = regressor.feature_importances_
	std = np.std([tree.feature_importances_ for tree in regressor.estimators_],
	             axis=0)
	indices = np.argsort(importances)[::-1]

	# Print the feature ranking
	print("Feature ranking:")

	with open('./train/train_result_'+resulttag+'.txt', 'w') as writer:
		for f in range(len(list(all_dataset_concat))):
		    writer.write('feat: '+str(list(all_dataset_concat)[f])+'\n')
		    writer.write('imp: '+str(std[f])+'\n')
		writer.write(res)
		writer.write('fpr\n')
		for n in fpr:
			writer.write(str(n)+'\n')
		writer.write('tpr\n')
		for n in tpr:
			writer.write(str(n)+'\n')
train('dataset2/data_processed/O_Thr_positive.csv', 'dataset2/data_processed/O_Thr_negative.csv', seqOnly = False, resulttag = 'O_Thr')
train('dataset2/data_processed/O_Thr_positive.csv', 'dataset2/data_processed/O_Thr_negative.csv', seqOnly = True, resulttag = 'O_Thr_with_seqeunce_only')
plt.title('O_Thr ROC')
plt.ylabel('tpr')
plt.xlabel('fpr')
plt.plot([0,1], [0,1], linestyle='dashed')
plt.legend(loc='upper left')
plt.show()
