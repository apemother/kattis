import sys

dictionary = {
'a': '@',
'b': '8',
'c': '(',
'd': '|)',
'e': '3',
'f': '#',
'g': '6',
'h': '[-]',
'i': '|',
'j': '_|',
'k': '|<',
'l': '1',
'm': '[]\/[]',
'n': '[]\[]',
'o': '0',
'p': '|D',
'q': '(,)',
'r': '|Z',
's': '$',
't': "']['",
'u': '|_|',
'v': '\/',
'w': '\/\/',
'x': '}{',
'y': '`/',
'z': '2'
}

for i in sys.stdin:
	ans = ''
	ab = list(i)
	for element in ab:
		element = element.lower()
		if element == '\n':
			break
		if element not in dictionary:
			ans += element
		else:
			ans += dictionary[element]
	print(ans)
