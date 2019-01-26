import csv
with open('./negative_dataset/N_neg_big.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		for k in row:
			print(k)
		break
