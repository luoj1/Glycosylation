import csv

input_addr = ['N_GO_CC_0119.txt', 'N_GO_BP_0119.txt', 'N_GO_MF_0119.txt', 'N_KEGG_0119.txt', 'N_PFAM_0119.txt', 'N_INTERACTION_0119.txt', 'N_INTERPRO_0119.txt']
output_addr = 'output_feature.csv'
featurelist_addr = 'feature_list.txt'
feature_tuple_set = set()
gene_set = set()
feat_set = set()
with open(output_addr, 'w') as csvfile:
	for addr in input_addr:

		with open(addr, 'r') as reader:
			line = reader.readline()
			line = reader.readline()
			while not line == '':
				row = line.split('	')[:-7]
				gene = row[5].split(',')
				#take out the first 7 stuff
				if float(row[4]) > 0.01:
					line = reader.readline()
					continue
				for g in gene:
					if g == '':
						continue
					gene_set.add(g)
					feature_tuple_set.add((row[1],g))
				feat_set.add(row[1])
				
				line = reader.readline()

	print('generating csv...')
	fieldnames = ['genes']
	for f in feat_set:
		fieldnames.append(f)
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	
	new_row = {}
	count = 0
	for g in gene_set:
		new_row['genes'] = g
		for f in feat_set:
			new_row[f] = int((f,g) in feature_tuple_set)
		count+= 1
		writer.writerow(new_row)
	print("count",count)

print('generate feature_list...')
with open(featurelist_addr, 'w') as file:
	for f in feat_set:

		file.write(f)
		file.write('\n')

			