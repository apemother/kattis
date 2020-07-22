import sys

x = 0
y = 0


for i in sys.stdin:
	ab = i.split()
	if len(ab) > 1:
		x = int(ab[3])
		y = int(ab[2])
		continue
		
	abc = list(ab[0])
	string = ""
	for elem in abc:
		for n in range(x):
			string += elem
	if y > 1:
		for n in range(y):
			print(string)
	else:
		print(string)
