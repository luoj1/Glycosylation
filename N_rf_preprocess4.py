import csv
collection_motif_pos = []
collection_unmotif_pos = []
collection_motif_neg = []
collection_unmotif_neg = []
header = []
header_flg = 0
with open("./dataset2/data_processed/N_positive.csv","r") as file:
	fc = csv.DictReader(file)
	for row in fc:
		if header_flg == 0:
			header = list(row)
			header_flg = 1
		if row['seq7_P'] == '0' and (row['seq8_S'] == '1' or row['seq8_T'] == '1'):
			collection_motif_pos.append(row)
		else:
			collection_unmotif_pos.append(row)
with open("./dataset2/data_processed/N_negative.csv","r") as file:
	fc = csv.DictReader(file)
	for row in fc:
		if row['seq7_P'] == '0' and (row['seq8_S'] == '1' or row['seq8_T'] == '1'):
			collection_motif_neg.append(row)
		else:
			collection_unmotif_neg.append(row)

with open("./dataset2/data_processed/N_motif_positive.csv","w") as file:
	fc = csv.DictWriter(file, fieldnames = header)
	fc.writeheader()
	for row in collection_motif_pos:
		fc.writerow(row)

with open("./dataset2/data_processed/N_unmotif_positive.csv","w") as file:
	fc = csv.DictWriter(file, fieldnames = header)
	fc.writeheader()
	for row in collection_unmotif_pos:
		fc.writerow(row)

with open("./dataset2/data_processed/N_motif_negative.csv","w") as file:
	fc = csv.DictWriter(file, fieldnames = header)
	fc.writeheader()
	for row in collection_motif_neg:
		fc.writerow(row)

with open("./dataset2/data_processed/N_unmotif_negative.csv","w") as file:
	fc = csv.DictWriter(file, fieldnames = header)
	fc.writeheader()
	for row in collection_unmotif_neg:
		fc.writerow(row)
