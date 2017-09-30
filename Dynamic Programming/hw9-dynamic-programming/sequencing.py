import doctest 

def lcsHelper(s1, s2, length = 0, copys1 = None, copys2 = None):
	'''
	Helper function to do the useIt or loseIt. 
	Necessary because we build up the strings as we recurse but return as soon as either string is empty
	Caller function appends the final number of # to the returned strings
	'''
	# initialize copies. We will store what we return here
	if copys1 == None:
		copys1 = ''
	if copys2 == None:
		copys2 = ''
	# base case: length of either string is 0
	if not s1 or not s2:
		return (length, copys1, copys2)

	if s1[0] == s2[0]:
		useIt = lcsHelper(s1[1:], s2[1:], length +1, copys1 + s1[0], copys2 + s2[0])
	else:
		useIt = (0, '', '')

	loseIt2 = lcsHelper(s1[1:], s2, length, copys1 + '#', copys2) # hash copys1
	loseIt1 = lcsHelper(s1, s2[1:], length, copys1, copys2 + '#') # hash other one

	return max(useIt, loseIt1, loseIt2)

def lcs(s1, s2):
	'''
	Returns tuple indicating length of lcs and copy of s1 and s2 with # marked for unused chars
	>>> lcs("human", "chimpanzee")
	(4, 'h#man', '#h#m#an###')
	>>> lcs("spam", "")
	(0, '####', '')
	>>> lcs("cat", "car")
	(2, 'ca#', 'ca#')
	'''
	answer = lcsHelper(s1, s2)
	# appends missing # characters to returned strings
	extraS1Hash = ''.join(['#' for i in range(len(s1) - len(answer[1]))])
	extraS2hash = ''.join(['#' for i in range(len(s2) - len(answer[2]))])

	return (answer[0], answer[1]+ extraS1Hash, answer[2] + extraS2hash)

def align(s1, s2, length = 0, copys1 = None, copys2 = None):
	'''
	Returns tuple of sequence alignment of two DNA strings along with length of lcs
	>>> align('spam', '')
	(0, 'spam', '----')
	>>> align('x', 'x')
	(1, 'x', 'x')
	>>> align('x', 'y')
	(0, 'x-', '-y')
	>>> align("cat", "car")
	(2, 'cat-', 'ca-r')
	>>> align("ATTGC", "GATC")
	(3, '-ATTGC', 'GAT--C')
	'''
	# initialize copies
	if copys1 == None:
		copys1 = ''
	if copys2 == None:
		copys2 = ''
	# base cases: length of either string is 0
	if not s1 or not s2:
		# return number of - characters equal to length of string that is not null
		return (length, copys1+s1, ''.join(['-' for i in range(len(s1))])) if not s2 else (length, ''.join(['-' for i in range(len(s2))]), copys2+s2)
	if s1 == s2: # strings are equal
		return (length + len(s1), copys1 + s1, copys2 + s2)
	if len(s1) == 1 and len(s2) == 1 and s1 != s2: # one character left but unequal strings
		return (length, copys1 + s1 + '-', copys2 + '-' + s2)

	if s1[0] == s2[0]:
		useIt = align(s1[1:], s2[1:], length + 1, copys1 + s1[0], copys2 + s2[0])
	else:
		useIt = (0, '', '')

	loseIt2 = align(s1[1:], s2, length, copys1 + s1[0], copys2 + '-')
	loseIt1 = align(s1, s2[1:], length, copys1 + '-', copys2 + s2[0])

	return max(useIt, loseIt1, loseIt2)

#print(doctest.testmod())


