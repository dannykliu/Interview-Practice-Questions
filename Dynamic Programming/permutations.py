def addChar(P, char):
    newP = []
    for string in P:
        for i in range(len(string)):
            newP.append(string[:i] + char + string[i:])
        newP.append(string + char)  # we miss last scenario where the char has to be appended to the end of the string
    # print(newP)
    return newP


def permutations(string):
    P = [string[0]]
    for char in string[1:]:
        P = addChar(P, char)
    print(P)
    return P


def addCharWithDup(P, char):
    newP = []
    # trick to get rid of duplicate strings as we create them instead of waiting till the end
    tempSet = set()
    for string in P:
        if string + char not in tempSet:
            newP.append(string + char)
            tempSet.add(string + char)
        for i in range(len(string)):
            temp = string[:i] + char + string[i:]  # line that creates weaving
            if temp not in tempSet:
                newP.append(temp)
                tempSet.add(temp)
    # print(newP)
    return newP


def permutationsWithDup(string):
    P = [string[0]]
    for char in string[1:]:
        P = addCharWithDup(P, char)
    print(P)
    return P


# addCharWithDup(['a'], 'c')
permutationsWithDup('aaaa')
