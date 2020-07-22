import sys

ops = {
	'-': lambda x, y: x-y,
	'+': lambda x, y: x+y,
	'*': lambda x, y: x*y
}

def isOperand(a):
	try:
		int(a)
		return True
	except ValueError:
		return False
		
def polish(expr, index):
	# operand otherwise operator
	if expr[index] not in ops:
		return expr[index], index+1
	op = expr[index]
	a, next_index = polish(expr, index+1)
	b, next_index = polish(expr, next_index)
	if isOperand(a) and isOperand(b):
		return str(ops[op](int(a), int(b))), next_index
	return ' '.join((op, a, b)), next_index

for n, i in enumerate(sys.stdin, start=1):
    ab = i.strip().split()
    ans, _ = polish(ab, 0)
    
    print('Case {}: {}'.format(n, ans))
