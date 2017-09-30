def powerSet(aList):  # [1, 2, 3]
    power_set = [[]]
    for element in aList:
        for sub_set in power_set:
            power_set = power_set + [sub_set + [element]]
    return power_set


def removeElements(old_target, remove):  # original, subset
    target = list(old_target)
    for element in remove:
        if element in target:
            target.remove(element)
    return target


def sameSums(aList):
    if len(aList) == 1 or len(aList) == 0:
        return False
    original = aList
    power_set = powerSet(aList)
    for subset in power_set:
        subtracted = removeElements(original, subset)
        if sum(subtracted) == sum(subset):
            return True
    return False


print(powerSet([2, 2, 500, 3, 3, 4, 4, 5, 5]))
