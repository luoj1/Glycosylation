from N_rf_helper import *
import os
import pandas as pd
src = [fn for fn in os.listdir("./dataset2/data")]
d2_translator_list = [fn for fn in os.listdir("./dataset2/translation")]
batch = []
for dt in d2_translator_list:
	name_resolver = dt.split('_')
	if not name_resolver[-1] == 'ext.csv':
		continue
	if name_resolver[-2] == 'elements':
		continue
	name_resolver = name_resolver[:-2]
	lbl =  name_resolver[-1]
	name_resolver = name_resolver[:-1]
	tp =  ''
	for n in name_resolver:
		tp +=n+'_'
	tp = tp[:-1] 
	batch.append(tp)


dictionary = './dataset2/translation/all_elements_ext.csv'
name2amino_matrix_batch_multiple(src, dictionary, batch,output = './dataset2/data_processed/')