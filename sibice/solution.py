import sys

num = 0
w = 0
h = 0

for i in sys.stdin:
	ab = i.split()
	if len(ab) > 1:
		num = int(ab[0])
		w = int(ab[1])
		h = int(ab[2])
	elif int(ab[0]) <= (w**2 + h**2)**0.5:
		print('DA')
	else:
		print('NE')
