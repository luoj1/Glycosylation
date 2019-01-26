import csv
import os
data_path = './negative_dataset'
res = os.listdir(data_path)
feature_file = 'negative_dataset/N_Negative_sequence.csv'
file_list = [ data_path + '/'+ f for f in res]
dest = 'negative_dataset/output.txt'
def features(file):
	out = set()
	with open(file, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			out.add((row['\ufeffEntry'] , row['site']))
	return out

def neg_feature_fetch(filelist, features, output):
	with open(output, 'w') as writer:
		for file in filelist:
			with open(file, 'r') as file:
				#omit first 20 rows
				for i in range (0,20):
					file.readline()
				#-------------------
				line  = file.readline()
				while not line == '':
					row = line
					line = line.split()
					try:
						name = line[2].split('_')[1]
					except:
						return
					site = line[3]
					if (name,site) in features:
						writer.write(row)
					line =file.readline()
feat = features(feature_file)
neg_feature_fetch(file_list, feat, dest)