import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
import os
import time
# read csv for preprocessing
# conver to np array
def preprocess():
	pos_data_path = "./dataset/positive"
	neg_data_path = "./dataset/negative"
	pos_file = os.listdir(pos_data_path)
	neg_file = os.listdir(neg_data_path)
	merge_path = './merge/'
	intersected = './merge/intersected/'
	print("="*20,"start rf","="*20)
	print("="*20,"timestamp ",int(time.time()),"="*20)
	god = """
	             ┏┓   ┏┓
	            ┏┛┻━━━┛┻┓
	            ┃   ☃   ┃
	            ┃ ┳┛ ┗┳ ┃
	            ┃   ┻   ┃
	            ┗━┓   ┏━┛
	              ┃   ┗━━━┓
	              ┃神兽保佑┣┓
	              ┃永无BUG!┏┛
	              ┗┓┓┏━┳┓┏┛
	               ┃┫┫  ┃┫┫
	               ┗┻┛  ┗┻┛
	"""             
	print(god)

	p_list = []
	n_list = []
	for item in pos_file:
		if item[0:4] == 'data' and item[len(item)-4:] == '.csv':
			p_list.append(item)
	for item in neg_file:
		if item[0:4] == 'data' and item[len(item)-4:] == '.csv':
			n_list.append(item)
	print(p_list)
	print(n_list)
	lis_buffer = []
	for csv in p_list:
		print('file pos ', csv)
		lis_buffer.append(pd.read_csv(pos_data_path+'/'+csv))
	p_list = lis_buffer.copy()
	lis_buffer = []
	for csv in n_list:
		print('file neg ', csv)
		lis_buffer.append(pd.read_csv(neg_data_path+'/'+csv))
	n_list = lis_buffer.copy()
	lis_buffer = []

	print('====finish putting pd to arrays====')
	return p_list, n_list


id_protocol = ['ID', [('id', 1), ('Uniprot accession',0), ('ID',0)]] # [1] of tuple means whether split fetch is needed
site_protocol = ['site', ['Site', 'n', 'site']]

def cut_id(src, col ,do,output =None):
	df  = pd.read_csv(src, index_col=0)
	counter = 0
	for i, row in df.iterrows():
		counter += 1
		if counter %100 == 0:
			print('count',counter)
		new_v = do(row[col])
		df.loc[i,col] = new_v
		#print('i',i)
		#print(new_v)
		
	print('finish edit id ', src)
	if not output == None:
		df.to_csv(output)

def concat_dataset(src, output = None):
	raw = [pd.read_csv(s) for s in src ]
	out = pd.concat(raw)
	if not output == None:
		out.to_csv(output)
	print('finish concat ', src)
	return out

def extend(base ,source, output = None):
	base_df = pd.read_csv(base)
	source_df = pd.read_csv(source)

	new_row = {}
	new_row['ID'] = []
	new_row['site'] = []
	for k in list(base_df):
		#for furtber optimization, it can change to a take-in lambda
		if not k == 'ID' and not k == 'site' and not k == '':
			new_row[k] = []
	'''
	for i, row in base_df.iterrows():
		for k in list(base_df):
			#for furtber optimization, it can change to a take-in lambda
			if not k == 'ID' and not k == 'site' and not k == '':
				new_row[k] = []
		break
	'''
	for k in list(source_df):
		#for furtber optimization, it can change to a take-in lambda
		if not k == 'id' and not k == 'n' and not k == '':
			new_row[k] = []
	'''
	for i, row in source_df.iterrows():
		for k in row:
			#for furtber optimization, it can change to a take-in lambda
			if not k == 'id' and not k == 'n' and not k == '':
				new_row[k] = []
		break
	'''

	#print([key for key in new_row])

	print('====finish init header===')
	counter = 0
	mem = {}

	for i, row in base_df.iterrows():
		#print(row)
		row_id = base_df.loc[i,'ID']
		row_site = base_df.loc[i,'site']
		q= 'n == "' + str(row_site)+ '"'
		if not row_id in mem:
			x = source_df[source_df.id.str.contains(row_id)]
			mem[row_id] = x
		else:
			x = mem[row_id] 
		x = x.query(q)
		if counter%1000==1:
			print('count: ', counter)
			#print(q)
			#print(x)
			
		counter+=1
		#print('====',len(x.index),'====')
		if len(x.index) > 0:

			for xi, xrow in x.iterrows():
				new_row['ID'].append(row_id)
				new_row['site'].append(row_site)
				for k in list(base_df):
					#print('key in row', k)
					#print('v in row', base_df.loc[i,k])
					if not k == 'ID' and not k == 'site' and k in new_row:
						new_row[k].append(base_df.loc[i,k])
				for k in list(source_df):
					#print('key in x', k)
					#print('v in x', source_df.loc[xi,k])
					if not k == 'id' and not k == 'n' and k in new_row:
						new_row[k].append(source_df.loc[xi,k])
				#print('add', row_id, row_site)
	out = pd.DataFrame(new_row)
	print('finsh', out.shape)
	if not output == None:
		out.to_csv(output)
	return out




def merge(li,logger,fn=None, debug_limit=False ):
	#fetch all header 
	curr_time = str(int(time.time()))
	print('=============merge() is called !!!!!=====================')
	header = set()
	# loop over ther file to build header
	for item in li:
		h = list(item)
		for sing in h: 
			header.add(sing)
	#remove various format of id
	for rand_id in id_protocol[1]:
		if rand_id[0] in header:
			header.remove(rand_id[0])
	#remove various format of site
	for rand_site in site_protocol[1]:
		if rand_id in header:
			header.remove(rand_id)
	#add genralzied id and site
	header.add(id_protocol[0])
	header.add(site_protocol[0])
	header = list(header)
	print('====finish preprocessing and header construction====')
	print('length: ', len(header))
	#row = [-1 for _ in range(len(header))]
	# ID & site and id & n
	out = pd.DataFrame(columns = header)
	#phase 1
	tracker = 0
	new_row = {}
	for df in li:
		print('start df', tracker)
		tracker += 1

		debug_it = 0
		for i, src in df.iterrows(): # handle row by row
			if debug_it%1000 == 0:
				print("debug_it count:", debug_it)
			if not debug_limit == False and debug_it > debug_limit:
				break
			#print(src.index)
			ID = None
			site = None
			# preprocess id and site
			for rand_id in id_protocol[1]:
				if rand_id[0] in src.index:
					if rand_id[1] == 1:
						ID = src[rand_id[0]].split('_')[1] # split and fetch
					else:
						ID = src[rand_id[0]] # orginal value

			for rand_site in site_protocol[1]:
				if rand_site in src.index:
					site = src[rand_site] #original value
			if ID == None:
				ID = src[id_protocol[0]]
			if site == None:
				site  = src[site_protocol[0]]
			logger.write( str(ID) + ": " + str(site) + '\n')
			#if exist in out 
			if len(out[out[id_protocol[0]].str.contains(ID)].index) > 0:
				tmp = out[out[id_protocol[0]].str.contains(ID)]
				if len(tmp[tmp[site_protocol[0]].str.contains(site)].index) > 0:
					ind = tmp[tmp[site_protocol[0]].str.contains(site)].index[0]
					logger.write( "exist: " + str(ID) + ": " + str(site) + '\n')
					for h in header: 
						logger.write("header: "+ h)
						logger.write('\n')
						if h == 'ID':
							pass
						elif h =='site':
							pass
						elif h in src.index:
							print(h, src[h])
							logger.write("found! val: "+ str(src[h]))
							logger.write('\n')
							out.loc[ind,h] = src[h]
						else:
							pass

					continue
			#otherwise
			#print(src.index)
			
			for h in header: 
				#h = h.lower()
				logger.write("header: "+ h)
				logger.write('\n')
				#print("header: "+ h)
				if h == id_protocol[0]:
					logger.write("found ID! val: "+ str(ID) )
					logger.write('\n')
					#new_row.append(str(ID))
					if h in new_row:
						new_row[h].append(str(ID))
					else:
						new_row[h] = [str(ID)]
				elif h == site_protocol[0]:
					logger.write("found site! val: "+ str(site))
					logger.write('\n')
					#new_row.append(str(site))
					#new_row[h] = str(site)
					if h in new_row:
						new_row[h].append(str(site))
					else:
						new_row[h] = [str(site)]
				elif h in src.index:
					logger.write("found! val: "+ str(src[h]))
					#print("found! val: "+ str(src[h]))
					logger.write('\n')
					#new_row.append(str(src[h]))
					#new_row[h] = str(src[h])
					if h in new_row:
						new_row[h].append(src[h])
					else:
						new_row[h] = [src[h]]
				else:
					#new_row.append(str(-1))
					if h in new_row:
						new_row[h].append(str(0))
					else:
						new_row[h] = [str(0)]
					#new_row[h] = str(-1)
			logger.write( "="*20 + "finish row" + "="*20  + '\n')
			#print("rowlen", len(new_row), "header",len(header))
			for h in header:
				logger.write("header:"+h+'\n')

			
			#new_df = pd.DataFrame(new_row, index=[0],columns=header)
			#out = out.append(new_df)
			#collector.append(new_row.copy())
			debug_it += 1
	#backup of merged file
	out = pd.DataFrame(new_row, columns=header)
	print(out.shape)
	if fn == None:
		out.to_csv(merge_path+"merged_"+curr_time+".csv")
	else:
		out.to_csv(merge_path+fn+".csv")
	return out
def intersect_df(list1,list2):
	header1 = list(list1)
	header2 = list(list2)
	head = set()
	for h in header1:
		head.add(h)
	for h in header2:
		if h in head:
			head.remove(h)
		else:
			head.add(h)
	#head = list(head)
	out1 = list1.copy()
	out2 = list2.copy()
	for h in head:
		if h in out1:
			out1 = out1.drop(columns=[h])
		else:
			out2 = out2.drop(columns=[h])
	return out1, out2

if __name__=='__main__':
	'''
	with open("merge_p_list.txt", "w") as logger:
		list1 = merge(p_list,logger,fn="merged_positive")
		print("finish p_list")
	'''
	'''
	list1 = pd.read_csv("./merge/merged_positive.csv")
	print("finish p_list")

	with open("merge_n_list.txt", "w") as logger:
		list2 = merge(n_list,logger,fn="merged_negative")
		print("finish n_list")
	list1, list2 = intersect_df(list1, list2)

	list1.to_csv(intersected+"processed_positive.csv")
	list2.to_csv(intersected+"processed_negative.csv")
	'''

	print('list1 header len: ' , len(list(list1)))
	print('list2 header len: ' , len(list(list2)))
	print('list1 len: ' , len(list1.index))
	print('list2 len: ' , len(list2.index))