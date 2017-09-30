import doctest

EGS = "GTACGTCGATAACTG"
WGS = "TGATCGTCATAACGT"

def lcs(s1, s2):
	'''
	>>> lcs("human", "chimpanzee")
	(4, 'h#man', '#h#m#an###')
	>>> lcs("spam", "")
	(0, '####', '')
	>>> lcs("cat", "car")
	(2, 'ca#', 'ca#')
	'''
	# base cases
	if not s1 and not s2:
		return (0, '', '')
	if not s1:
		return (0, '', ''.join(['#' for i in range(len(s2))]))
	if not s2:
		return (0, ''.join(['#' for i in range(len(s1))]), '')

	# answers to original problem - bottom up recursion
	useIt = lcs(s1[1:], s2[1:])
	loseIt2 = lcs(s1[1:], s2)
	loseIt1 = lcs(s1, s2[1:])

	# compute new answers based on old answers
	if s1[0] == s2[0]:
		useIt = (1 + useIt[0], s1[0] + useIt[1], s2[0] + useIt[2])
	else:
		useIt = (0, '', '')

	loseIt2 = (loseIt2[0], '#' + loseIt2[1], loseIt2[2])
	loseIt1 = (loseIt1[0], loseIt1[1], '#' + loseIt1[2])

	return max(useIt, loseIt2, loseIt1)

def align(s1, s2):
	'''
	>>> align('spam', '')
	(0, 'spam', '----')
	>>> align('x', 'x')
	(1, 'x', 'x')
	>>> align('x', 'y')
	(0, '-x', 'y-')
	>>> align("cat", "car")
	(2, 'ca-t', 'car-')
	>>> align("ATTGC", "GATC")
	(3, '-ATTGC', 'GAT--C')
	'''
	# base cases
	if s1 == s2:
		return (len(s1), s1, s2)
	if not s1 and not s2:
		return (0, '', '')
	if not s1:
		return (0, ''.join(['-' for i in range(len(s2))]), s2)
	if not s2:
		return (0, s1, ''.join(['-' for i in range(len(s1))]))
	if len(s1) == 1 and len(s2) == 1:
		return (0, '-' + s1, s2 + '-')

	# answers to original problem
	useIt = align(s1[1:], s2[1:])
	loseIt2 = align(s1[1:], s2)
	loseIt1 = align(s1, s2[1:])

	# compute new answers using old answers
	if s1[0] == s2[0]:
		useIt = (1 + useIt[0], s1[0] + useIt[1], s2[0] + useIt[2])
	else:
		useIt = (0, '', '')

	loseIt2 = (loseIt2[0], s1[0] + loseIt2[1], '-' + loseIt2[2])
	loseIt1 = (loseIt1[0], '-' + loseIt1[1], s2[0] + loseIt1[2])

	return max(useIt, loseIt2, loseIt1)

print(doctest.testmod())
