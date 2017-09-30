def powerSet(aList):  # [1, 2, 3]
    pset = [[]]
    for element in aList:
        for subset in pset:
            pset += [
                subset + [element]]  # creates new variable pset everytime, does not affect currently iterating pset
    return pset


def powerSetComp(L):
    pset = [[]]
    for e in L:
        pset += [s + [e] for s in pset]
    return pset


def recursiveMultiply(a, b):
    if b == 0:
        return 0
    return a + recursiveMultiply(a, b - 1)


print(powerSetComp([1, 2, 3]))
print(recursiveMultiply(5, 5))
