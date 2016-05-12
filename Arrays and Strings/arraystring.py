def is_unique(string):
	freq = [0]*128 
	for char in string:
		if(freq[ord(char)] == 0):
			freq[ord(char)] += 1
		else:
			return False
	return True

def is_permutation(s1, s2):
	f1 = [0]*128
	f2 = [0]*128
	for char in s1:
		f1[ord(char)]+=1
	for char in s2:
		f2[ord(char)]+=1
	return f1 == f2

def urlify(string, length):
	string = list(string)
	extra_spaces = len(string) - length
	for i in range(length-1, -1, -1):
		if(string[i] != " "):
			string[i+extra_spaces] = string[i]
		else:
			string[i+extra_spaces] = "0"
			string[i+extra_spaces-1] = "2"
			string[i+extra_spaces-2] = "%"
			extra_spaces -= 2
	return ''.join(string)

def palindrome_permutation(string):
	string = string.lower()
	string = string.replace(' ', '')
	freq = [0]*128 
	for char in string:
			freq[ord(char)] += 1
	num_singles = 0
	for num in freq:
		if(num %2 == 1):
			num_singles += 1
		if(num_singles >1):
			return False
	return True

def one_away(s1, s2):
	num_away = 0
	if(len(s1) == len(s2)):
		for i in range(len(s1)):
			if(s1[i] != s2[i]):
				num_away+=1
			if(num_away >1): return False
	elif(len(s1) == len(s2)+1):
		for i in range(len(s2)):
			if(s1[i+num_away] != s2[i]):
				num_away += 1
				i -= 1
			if(num_away >1): return False
	elif(len(s2) == len(s1) +1):
		for i in range(len(s1)):
			if(s2[i+num_away] != s1[i]):
				num_away += 1
				i -= 1
			if(num_away >1): return False
	else:
		return False
	return True

def string_compression(string):
	string += ' '
	new_string = ''
	num_chars = 1
	for i in range(len(string) - 1):
		if(string[i] == string[i+1]):
			num_chars += 1
		else:
			new_string += string[i] + str(num_chars)
			num_chars = 1
	if(len(new_string) < len(string) -1):
		return new_string
	else:
		return string[:len(string)-1] #chop off extra char

def rotate_90(matrix):
	n = len(matrix)
	for i in range(n/2): #swap rows
		temp = matrix[i]
		matrix[i] = matrix[n-1]
		matrix[n-1] = temp
	for r in range(n): #transpose
		for c in range(r, n):
			temp = matrix[r][c]
			matrix[r][c] = matrix[c][r]
			matrix[c][r] = temp
	return matrix

def zero_matrix(matrix):
	coords = []
	for r in range(len(matrix)):
		for c in range(len(matrix[r])):
			if(matrix[r][c] == 0):
				coords.append((r, c))
	for coord in coords:
		matrix[coord[0]] = [0]*len(matrix[coord[0]]) #set row to 0
		for r in range(len(matrix)):
				matrix[r][coord[1]] = 0 #set col to 0
	return matrix

def string_rotation(s1, s2):
	s1 *= 2 # add s1 to itself
	if(len(s1)/2 == len(s2) and s1.find(s2) >= 0):
		return True
	return False

print string_rotation("waterbottle", "erbottlewat")
