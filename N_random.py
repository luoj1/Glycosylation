import random

input_address = 'N_negative_sequence.txt'
output_address = 'output_random.txt'
output_size = 7000

with open(input_address, 'r') as reader:
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
			if c == 'N' and  N_index >= 7:
				buff.append((_id, str(N_index)))
			N_index += 1

		seq_length  = N_index - 1
		# take out last 7 numbers
		for i in range(len(buff)-1, len(buff)-8, -1):
			if i <0:
				break
			if buff[i][0] == _id and int(buff[i][1]) > seq_length-7:
				buff.pop(len(buff)-1)
			else:
				break

		line = reader.readline()
	print('sampling finished')

	
	with open(output_address,'w') as writer:
		size = 0
		no_repeat = set()
		while size < output_size and not len(no_repeat) == len(buff):
			item = random.choice(buff)
			if item in no_repeat:
				continue
			writer.write(item[0]+'	')
			writer.write(item[1])
			writer.write('\n')
			no_repeat.add(item)
			size+=1
		print('output: ', size)
			

	