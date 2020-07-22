import sys

for i in sys.stdin:
	ab = i.split()
	binary = list(bin(int(ab[0])))
	rev_bin = ""
	for n in range(len(binary)-2):
		rev_bin += str(binary[len(binary)-n-1])
	rev_dec = int(rev_bin, 2)
	print(rev_dec)
