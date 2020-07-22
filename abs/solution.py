import sys

for i in sys.stdin:
	ab = i.split()
	x1 = float(ab[0])
	if x1 == 0:
		break
	y1 = float(ab[1])
	x2 = float(ab[2])
	y2 = float(ab[3])
	p = float(ab[4])
	print( ( abs( x1 - x2 ) ** p + abs( y1 - y2 ) ** p ) ** (1 / p) )
	
# (|x1−x2|p+|y1−y2|p)1/p

# sample input
# 1.0 1.0 2.0 2.0 2.0
# 1.0 1.0 2.0 2.0 1.0
# 1.0 1.0 20.0 20.0 10.0

# sample output
# 1.4142135624
# 2.0000000000
# 20.3636957882
