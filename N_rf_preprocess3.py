import csv
import subprocess
import pandas as pd
import os
translation = dict()
output_collections = dict() #key (key, label)
#os.remove("*_bitmapped.csv")

with open("./dataset2/translation/all_elements_ext.csv", "r") as file:
	#read line
	#(type, status): dict
	#dict -> id, sequence
	reader = csv.DictReader(file)
	for row in reader:
		if not (row["type"],row["label"]) in translation:
			#translation[(row["type"],row["label"])] = dict()
			output_collections[(row["type"],row["label"])] = []
		#translation[(row["type"],row["label"])][(row["ID"],row["site"])] = row["sequence"]
		#O43451 1778
		translation[(str(row["ID"]),str(row["site"]))] = (row["sequence"],row["type"],row["label"])

print("finish building set ", len(translation))

src = [ fn if not fn == '.DS_Store' else None for fn in os.listdir("./dataset2/data")]
print(src)
folder = './dataset2/data/'
out = './dataset2/data_processed/'
dest = [ k[0]+'_'+k[1]+'.csv' for k in output_collections]
dest_info = [ (k[0],k[1]) for k in output_collections]

'''
for f in src:
	tmp = f.split('.')
	dest.append(tmp[0]+'_bitmapped.csv')

	#subprocess.run(["cat", folder+f, ">>",out+tmp[0]+'_bitmapped.csv'])
'''
print("finish file copy")
#add extra column
header = [] 
header_flg = 0
amino = ['R', 'H', 'K', 'D', 'E', 'S', 'T', 'N', 'Q', 'C', 'U' ,'G', 'P', 'A', 'V', 'I','L','M','F','Y','W']
seq_len = 14
for i in range(seq_len):
		header += [ 'seq'+str(i)+'_'+a for a in amino]
with open(folder+src[0], "r") as rfile:
	reader = csv.DictReader(rfile)
	for row in reader:
		header += list(row)
		break

header += ['type','label', 'ID', 'site']

for h in output_collections:
	output_collections[h] = []
print("finish building header")
#for d in dest:
#	csv_df = pd.read_csv(d,index_col = 0)
def seq2dict(seq):
	ind = 0
	out = dict()
	for s in seq:
		out['seq'+str(ind)+'_'+s] = 1
		ind += 1
	return out

for filename in src:
	if filename == None:
		continue
	print('on ', folder+filename)
	with open(folder+filename, "r") as rfile:
		reader = csv.DictReader(rfile)
		for row in reader:
			#print(row)

			if not (row['id'].split('_')[1], str(row['n'])) in translation:
				#print("missing ", row['id'].split('_')[1], row['n'])
				continue
			seq, tp, lbl = translation[(row['id'].split('_')[1], str(row['n']))]
			bm = seq2dict(seq)			
			row.update(bm)
			row.update({'type': tp, 'label': lbl, 'ID': row['id'].split('_')[1], 'site': row['n']})
			output_collections[(tp, lbl)].append(row)
print("write")

for filename, k in zip(dest,dest_info):
	print('write ',out+filename)
	with open(out+filename,'w') as wfile:
		writer = csv.DictWriter(wfile, fieldnames = header, restval= '0')
		writer.writeheader()
		for r in output_collections[k]:
			writer.writerow(r)
		#make translation
		#extend header
		#translate seq to bitmap

