arr = [] 
with open("./train_result.txt", "r") as read:
	line1 = read.readline()
	line2 = read.readline()
	while not line1 == '' and not line2 == '':
		arr.append((float(line2.split(':')[1]),line1.split(':')[1]))

		line1 = read.readline()
		line2 = read.readline()

arr.sort()
arr = arr[::-1]
for e in arr:
	print(e)