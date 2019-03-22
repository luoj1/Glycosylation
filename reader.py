import csv
import pandas as pd
'''
with open('neg-merge/N_Negative_sequence_1.csv', 'r') as file:
	reader = csv.DictReader(file)
	for row in reader:
		print(row)
		break
'''
# with open('neg-merge/N_neg_sample.csv', 'r') as file:
# 	reader = csv.DictReader(file)
# 	for row in reader:
# 		print(row)
# 		break

r1 = []
r2 = []

'''
print("="*50)
with open('dataset/negative/data_N_neg_1_2000_result_1.csv', 'r') as file:
	reader = csv.DictReader(file)
	for row in reader:
		r1 = list(row)
		break
print("="*50)
with open('dataset/negative/data_N_neg_2001_4776_result.csv', 'r') as file:
	reader = csv.DictReader(file)
	for row in reader:
		r2 = list(row)
		break

print("r1 len", len(r1))
print("r2 len", len(r2))
for x in r1:
	if not x in r2:
		print('extra in r1',x)


print("="*50)
with open('dataset/negative/data_N_Negative_sequence_2.csv', 'r') as file:
	
	reader = csv.DictReader(file)
	counter = 0
	for row in reader:
		x = list(row)[:10]
		print(x)
		break
		#counter+=1
	print('neg:', counter)


with open('dataset/negative/data_concated_cut_id.csv') as file:
	reader = csv.DictReader(file)

	counter = 0
	for row in reader:
		x = list(row)[:10]
		print(x)
		out  = []
		for k in x:
			out += [row[k]] 
		print(out)
		if counter < 5:
			counter+=1
		else:
			break
'''
#df = pd.read_csv('dataset/negative/data_N_Negative_sequence_2.csv')
source_df = pd.read_csv('dataset/negative/data_concated.csv', index_col=0)
row_site = '2'
row_id = 'A0A024RBG1'
q= 'n == "' + str(row_site)+ '"'
x = source_df[source_df.id.str.contains(row_id)]
x = x.query(q)
print(x)
print('length',len(x.index))

'''
row_site = '243'
row_id = 'A0A024RBG1'
q= 'id == "'+str(row_id)+'" & n == "' + str(row_site)+ '"'
x = source_df[source_df.id.str.contains(row_id)]
x = x[x.n.str.match(row_site)]
print(x)
print('length',len(x.index))
'''

with open('dataset/negative/data_concated.csv') as file:
	reader = csv.DictReader(file)
	counter = 0
	#for row in reader:
		#counter+=1
	print('dc:', counter)

'''
print("="*50)
with open('dataset/positive/data_positive_feature.csv', 'r') as file:
	reader = csv.DictReader(file)
	for row in reader:
		print(row["Uniprot accession"])
		x = list(row)[:10]
		print(x)
		out  = []
		for k in x:
			out += [row[k]] 
		print(out)
		break
'''
#https://drive.google.com/file/d/17cusFQB_56-eOogcZzCroKZ7ibnX6h2C/view?usp=sharing_eil&amp;ts=5c5b5c55