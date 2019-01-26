with open('N_negative_sequence.txt', 'r') as reader:
	reader.readline()
	buff = []
	line = reader.readline()
	while not line == '':
		arr = line.split()
		_id = arr[0]
		count = 0
		seq = ''
		if len(arr) == 1:
			seq = reader.readline()
		else:
			seq = arr[1]

		N_index = 1
		for c in seq:
			if c == 'N':
				buff.append((_id, str(N_index)))
			N_index += 1
		line = reader.readline()
	buff.sort()
	with open('output_index.txt','w') as writer:
		for item in buff:
			writer.write(item[0]+'	')
			writer.write(item[1])
			writer.write('\n')
			
