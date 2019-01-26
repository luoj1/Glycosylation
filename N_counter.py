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
		for c in seq:
			if c == 'N':
				count += 1
		buff.append((_id, str(count)))
		line = reader.readline()
	buff.sort()
	with open('output_counter.txt','w') as writer:
		for item in buff:
			writer.write(item[0]+'	')
			writer.write(item[1])
			writer.write('\n')
			
