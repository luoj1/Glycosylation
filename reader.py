import csv

with open('neg-merge/N_Negative_sequence_1.csv', 'r') as file:
	reader = csv.DictReader(file)
	for row in reader:
		print(row)
		break

with open('neg-merge/N_neg_sample.csv', 'r') as file:
	reader = csv.DictReader(file)
	for row in reader:
		print(row)
		break