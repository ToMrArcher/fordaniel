import random

count = 0

data = [[],[],[],[],[],[]]

for x in range(6):
	for y in range(512):
		data[x].append(random.randint(0,9))


for x in range(len(data) - 1):
	print(f"DATA {x}: ")
	for y in range(len(data[x])):
		print(data[x][y], sep=' ', end='', flush=True)
		count += 1
	print("\n")

for x in range(len(data[-1])):
	if count >= 3000:
		break
	else:
		print(data[-1][x], sep=' ', end='', flush=True)
		count += 1

print(f'\n\nCount = {count}')



