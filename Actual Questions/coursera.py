def balanceSum(A):
	leftSum = 0
	rightSum = sum(A) - A[0]
	for i in range(len(A)):
		if leftSum == rightSum:
			return i +1
		if i+1 < len(A):
			leftSum += A[i]
			rightSum -= A[i+1]

def isPalindrome(string):
	start = 0
	end = len(string)-1
	while start < end:
		if string[start] != string[end]:
			return False
		start += 1
		end -= 1
	return True

def palindrome(str):
	count = 0
	substrings = set()
	for i in range(len(str)):
		for j in range(i, len(str)):
			currString = str[i:j + 1]
			if currString not in substrings and isPalindrome(currString):
				count += 1
				substrings.add(currString)
	return count


print palindrome('aabaa')

