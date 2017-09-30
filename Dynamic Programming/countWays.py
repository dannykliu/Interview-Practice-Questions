# recursive 3^n solution
def countWaysRecursive(n):
    if n < 0:
        return 0
    elif n is 0:
        return 1
    return countWaysRecursive(n - 1) + countWaysRecursive(n - 2) + countWaysRecursive(n - 3)


def countWaysDP(n):
    A = [1, 1, 2]
    if n < len(A):
        return A[n]
    it = len(A)
    while n >= len(A):
        A.append(A[it - 1] + A[it - 2] + A[it - 3])
        it += 1
    print(A)
    return A[n]


print(countWaysDP(6))
