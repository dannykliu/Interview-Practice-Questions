import pandas as pd 
import doctest

WORD_LIST_FILE = '3esl.txt'
HITS = 10

def getValue(mat, first, second, r, c):
	'''
	Computes the next cell in the dp matrix
	'''
	minVal = 1 + min(mat[r-1][c-1], mat[r][c-1], mat[r-1][c])
	return minVal if first[r] != second[c] else mat[r-1][c-1]

def dynamicEditDistance(first, second):
	'''
	Returns the mininum number of edits necessary to change from first to second
	>>> dynamicEditDistance("xylophony", "yellow")
	7
	>>> dynamicEditDistance("antidisestablishment", "antiquities")
	13
	>>> dynamicEditDistance("follow", "yellow")
	2
	'''
	first = ' ' + first # makes our base cases work better
	second = ' ' + second
	mat = [[0 for x in range(len(second))] for y in range(len(first))] # create matrix
	# compute base cases
	mat[0][0] = 0 if first[0] == second[0] else 1
	for r in range(1, len(mat)):
		mat[r][0] = 1 + mat[r-1][0] 
	for c in range(1, len(mat[0])):
		mat[0][c] = 1 + mat[0][c-1] 
	# start dp
	for r in range(1, len(mat)):
		for c in range(1, len(mat[0])):
			mat[r][c] = getValue(mat, first, second, r, c)

	#print(pd.DataFrame(mat))
	return mat[-1][-1]

def addToList(L, word, result):
	'''
	Adds result to L if the edit distance from it to word is less than that of the maximum edit distance in L 
	'''
	eD = dynamicEditDistance(word, result) # compute edit distance
	if len(L) < HITS:
		L.append((eD, word)) # always add for first 10
	if L: worst = max(L)
	if len(L) >= HITS and eD < worst[0]: # only add to L if better than worst case
		L.remove(worst)
		L.append((eD, word))

def main():
	'''
	Runs spell checking process and returns top 10 words with shortest distance. Terminates on enter
	'''
	wordList = open(WORD_LIST_FILE).read().split('\n')
	while 1:
		result = str(input('spell check> '))
		if result == '':
			break # end process
		elif result in wordList:
			print('Correct')
		else:
			topTen = []
			print('Suggested alternatives:')
			for word in wordList:
				addToList(topTen, word, result)
			topTen = sorted(topTen)
			for word in topTen:
				print(word[1])

	return 0

#print(doctest.testmod())

if __name__ == '__main__':
	main()
