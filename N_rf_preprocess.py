from N_rf_helper import *
concat_arr1 = ['dataset/negative/data_N_neg_1_2000_result_1.csv',
				'dataset/negative/data_N_neg_2001_4776_result.csv']
#concat_dataset(concat_arr1, output='dataset/negative/data_concated.csv')
#cut_id('dataset/negative/data_concated.csv', 'id',
# lambda v:  v.split('_')[1], output = 'dataset/negative/data_concated_cut_id.csv')
#extend('dataset/negative/data_N_Negative_sequence_2.csv',
# 'dataset/negative/data_concated_cut_id.csv', output = 'merge/merged_negative2.csv')

intersected = './merge/intersected/'
'''
list1 = pd.read_csv("./merge/merged_positive.csv")
list2 = pd.read_csv("./merge/merged_negative2.csv")
list1, list2 = intersect_df(list1, list2)
list1.to_csv(intersected+"processed_positive.csv")
list2.to_csv(intersected+"processed_negative.csv")
'''

list1 = pd.read_csv(intersected+"processed_positive.csv", index_col=0)
list2 = pd.read_csv(intersected+"processed_negative.csv",index_col= 0)
droplist = []
for k in list(list1):
	if not (k == 'ID' or k == 'site' or (len(k)>0 and k[0] == 'X')):
		droplist.append(k)

list1 = list1.drop(columns = droplist)
list2 = list2.drop(columns = droplist)


list1.to_csv(intersected+"processed_positive_noGO.csv")
list2.to_csv(intersected+"processed_negative_noGO.csv")
