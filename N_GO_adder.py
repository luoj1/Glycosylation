import csv
import shutil
additional_chem = ['N_negative_feature_DAVID.txt']

feature_tuple = set()
allfeatures = []
chem_set = set()
with open('feature_list.txt', 'r') as f:
	line = f.readline()
	while not line == '':
		allfeatures.append(line)
		line = f.readline()
for addr in additional_chem:
	with open(addr, 'r') as f:
		line = f.readline()
		line = f.readline()
		while not line == '':
			row = line.split('	')
			chem = row[0]
			chem_set.add(chem)
			for feat in row[3:]:
				feat = feat.split(',')
				for ft in feat:
					if not ft == '':
						feature_tuple.add((chem,ft))
			line = f.readline()

with open('output_feature_neg.csv', 'w') as f:
	writer  = csv.DictWriter(f, fieldnames=['genes']+allfeatures)
	writer.writeheader()
	new_row = {}
	for c in chem_set:
		new_row['genes'] = c
		for ft in allfeatures:
			new_row[ft] = int((c,ft) in feature_tuple)
		writer.writerow(new_row)
