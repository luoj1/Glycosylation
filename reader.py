import csv
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

print("="*50)
with open('dataset/negative/data_N_neg_1_2000_result_1.csv', 'r') as file:
	reader = csv.DictReader(file)
	for row in reader:
		x = list(row)[:10]
		print(x)
		out  = []
		for k in x:
			out += [row[k]] 
		print(out)
		break
print("="*50)
with open('dataset/negative/data_N_neg_2001_4776_result.csv', 'r') as file:
	reader = csv.DictReader(file)
	for row in reader:
		x = list(row)[:10]
		print(x)
		out  = []
		for k in x:
			out += [row[k]] 
		print(out)
		break
print("="*50)
with open('dataset/negative/data_N_Negative_sequence_2.csv', 'r') as file:
	reader = csv.DictReader(file)
	for row in reader:
		x = list(row)[:10]
		print(x)
		out  = []
		for k in x:
			out += [row[k]] 
		print(out)
		break
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

#https://drive.google.com/file/d/17cusFQB_56-eOogcZzCroKZ7ibnX6h2C/view?usp=sharing_eil&amp;ts=5c5b5c55