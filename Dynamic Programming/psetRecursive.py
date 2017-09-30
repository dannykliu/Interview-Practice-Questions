'''
Given an array of ints, determine if it is possible to divide the numbers into 
two groups so that the sums of the two groups are the same. 
Every number must be in one group or the other.  

             sameSums([4, 7, 6, 3]) --> True    //4+6 = 10  and 7 + 3 = 10

             sameSums([3, 3]) -->  True

             sameSums([4, 12, 16])  --> True    //4+12= 16 and 16

             sameSums([5, 1]) --> False

'''


def removeElements(old_target, remove):  # original, subset
    target = old_target[:]  # make copy of list
    for element in remove:
        if element in target:
            target.remove(element)
    return target


def checkSubsetsOfPsets(original, pset):
    for subset in pset:
        subtracted = removeElements(original, subset)
        if sum(subtracted) == sum(subset):
            return True
    return False


# could also check if any subset in the pset is equal to total sum/2
def sameSums(aList, pset=None, original=None):
    if pset == None:
        pset = [[]]
    if original == None:
        original = aList
    if len(aList) == 0:
        return checkSubsetsOfPsets(original, pset)
    element = aList[0]
    lengthOfPset = len(pset)
    for i in range(lengthOfPset):
        newset = pset[i] + [element]
        pset.append(newset)
    return sameSums(aList[1:], pset, original)


# print sameSums([2, 400, 2, 3, 3, 4, 4, 5, 5])
# print sameSums([1, 7, 2, 4, 3, 6]) 
print(sameSums([10, 0]))
# print sameSums([1, 9, 5, 9])
# print sameSums([2, 2, 3, 3, 4, 4, 1, 1])
# print sameSums([])
# print sameSums([9, 1, 10])
