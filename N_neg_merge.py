import pandas as pd 
import numpy as np 

sample = pd.read_csv("neg-merge/N_neg_sample.csv")
entry = pd.read_csv("neg-merge/N_Negative_sequence_1.csv")

entry_set = set()

for i in range( entry.size//len(list(entry))):
	temp = entry.at[i, 'Entry']
	entry_set.add((temp, entry.at[i ,'site']))
header = list(sample)
print(header)
out = pd.DataFrame(columns=header)


for i in range( sample.size//len(list(sample))):
	id_temp = sample.at[i, 'id']
	id_temp = id_temp.split('_')
	id_temp = id_temp[1]
	print(id_temp)
	if (id_temp,sample.at[i, 'n'] ) in entry_set:
		n = pd.DataFrame([list(sample.loc[0])],columns=header)
		out.append(n)

out.to_csv(path_or_buf='./output_neg_merge.csv')
