from N_rf_helper import *
import os
import pandas as pd
concat_arr1 = ['dataset/negative/data_N_neg_1_2000_result_1.csv',
				'dataset/negative/data_N_neg_2001_4776_result.csv']
d2_translator_list = [fn for fn in os.listdir("./dataset2/translation")]
mem = {"ID":[],"site":[],"sequence":[],"type":[],"label":[]}
print(d2_translator_list)
for dt in d2_translator_list:
	name_resolver = dt.split('_')
	name_resolver = name_resolver[:-1]
	lbl =  name_resolver[-1]
	name_resolver = name_resolver[:-1]
	tp =  ''
	for n in name_resolver:
		tp +=n+'_'
	tp = tp[:-1] 
	print('type',tp)
	print('label', lbl)
	fn = 'dataset2/translation/' + str(dt)
	print(fn)
	p = pd.read_csv(str(fn),encoding = "utf-8")
	newrow = {"ID":[],"site":[],"sequence":[],"type":[],"label":[]}
	for i, row in p.iterrows():
		newrow['ID'].append(p.loc[i,'ID'])
		newrow['site'].append(p.loc[i,'site'])
		newrow['sequence'].append(p.loc[i,'sequence'])
		newrow['type'].append(tp)
		newrow['label'].append(lbl)
		mem['ID'].append(p.loc[i,'ID'])
		mem['site'].append(p.loc[i,'site'])
		mem['sequence'].append(p.loc[i,'sequence'])
		mem['type'].append(tp)
		mem['label'].append(lbl)

	out = pd.DataFrame(newrow)
	print('finsh', out.shape)
	out.to_csv("dataset2/translation/" + dt.split('.')[0]+'_ext.csv')
out = pd.DataFrame(mem)
out.to_csv("dataset2/translation/" + 'all_elements_ext.csv')
print('finsh', out.shape)
#concat_dataset(concat_arr1, output='dataset/negative/data_concated.csv')
#cut_id('dataset/negative/data_concated.csv', 'id',
# lambda v:  v.split('_')[1], output = 'dataset/negative/data_concated_cut_id.csv')
#extend('dataset/negative/data_N_Negative_sequence_2.csv',
# 'dataset/negative/data_concated.csv', output = 'merge/merged_negative2_test.csv')

intersected = './merge/intersected/'
'''
list1 = pd.read_csv("./dataset/positive/data_positive_1.csv")
list1  = list1.rename(columns = 
         {'Uniprot accession' : 'ID','Site':'site'})
list1.to_csv("./merge/merged_positive2.csv")
'''
'''
list1 = pd.read_csv("./merge/merged_positive2.csv", index_col=0)
list2 = pd.read_csv("./merge/merged_negative2_test.csv", index_col=0)
list1, list2 = intersect_df(list1, list2)
list1.to_csv(intersected+"processed_positive2.csv")
list2.to_csv(intersected+"processed_negative2.csv")
'''

'''
list1 = pd.read_csv(intersected+"processed_positive2.csv", index_col=0)
list2 = pd.read_csv(intersected+"processed_negative2.csv",index_col= 0)
droplist = []
for k in list(list1):
	if not (k == 'ID' or k == 'site' or (10>len(k)>0)):
		droplist.append(k)
	elif k[0] == 'X':
		droplist.append(k)

list1 = list1.drop(columns = droplist)
list2 = list2.drop(columns = droplist)

list1.to_csv(intersected+"processed_positive2_secondaryOnly.csv")
list2.to_csv(intersected+"processed_negative2_secondaryOnly.csv")
'''
#name2amino_matrix(intersected+"processed_positive2_secondaryOnly.csv",'./translation/neg_pos_sequence.csv',output=intersected+"processed_positive2_matrix.csv")
#name2amino_matrix(intersected+"processed_negative2_secondaryOnly.csv",'./translation/neg_pos_sequence.csv',output=intersected+"processed_negative2_matrix.csv" )


