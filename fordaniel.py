import random

count = 0

data = [[],[],[],[],[],[]]

#creates random numbers to put in data bank
for x in range(6):
	for y in range(512):
		data[x].append(random.randint(0,9))

#prints out the first 5 caches and increments a count.
for x in range(len(data) - 1):
	print(f"DATA {x}: ")
	for y in range(len(data[x])):
		print(data[x][y], sep=' ', end='', flush=True)
		count += 1
	print("\n")

#prints out last cache, until the count equals 3000
for x in range(len(data[-1])):
	if count >= 3000:
		break
	else:
		print(data[-1][x], sep=' ', end='', flush=True)
		count += 1

#prints out the count
print(f'\n\nCount = {count}')



