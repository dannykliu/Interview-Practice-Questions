import sys
import doctest


def change(amount, coins):
    '''
	Given an amount of change and a list of currencies, return the minimum number
	of coins needed to make the change, using an unlimited amount of the provided
	currencies. If no change can be made using the currencies, return infinity
	>>> change(50, [1, 7, 24, 42])
	3
	>>> change(50, [])
	9223372036854775807
	>>> change(5, [1, 3, 4])
	2
	'''
    if len(coins) == 0 and amount != 0 or amount < 0:
        return sys.maxsize
    if amount == 0:
        return 0
    useIt = 1 + change(amount - coins[0], coins)
    loseIt = change(amount, coins[1:])

    return min(useIt, loseIt)  # best performance of both strategies will give us our answer


def changeDP(amount, coins):
    '''
	>>> changeDP(50, [1, 7, 24, 42])
	3
	>>> changeDP(50, [])
	9223372036854775807
	>>> changeDP(5, [1, 3, 4])
	2
	'''
    if amount <= 0:
        return 0
    # dp array is of size n + 1
    dp = [0] * (amount + 1)
    # each cell i represents the min no. of coins needed to make i cents
    dp[0] = 0
    for i in range(1, len(dp)):
        dp[i] = min([sys.maxsize] + [1 + dp[i - coin] for coin in coins if coin <= i])

    return dp[-1]


def makeCents(amount, coins):
    '''
	Finds number of possible ways to make n cents given a list of coin values
	>>> makeCents(5, [25, 10, 5, 1])
	2
	>>> makeCents(10, [25, 10, 5, 1])
	4
	>>> makeCents(15, [25, 10, 5, 1])
	6
	>>> makeCents(20, [25, 10, 5, 1])
	9
	'''
    if amount == 0:
        return 1
    if not coins or amount < 0:
        return 0
    useIt = makeCents(amount - coins[0], coins)
    loseIt = makeCents(amount, coins[1:])

    return useIt + loseIt


def makeCentsDP(amount, coins):
    if amount <= 0:
        return 0
    dp = [0] * (amount + 1)  # dp array of size n+1
    # each cell i represents the no. of ways to make i cents
    dp[0] = 1
    for i in range(1, len(dp)):
        dp[i] = len([dp[i - coin] for coin in coins if coin <= i])

    return dp


# print(makeCents(20, [25, 10, 5, 1]))
print(makeCentsDP(11, [25, 10, 5, 1]))
# print(doctest.testmod())
