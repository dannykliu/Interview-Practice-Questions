def editDistance(first, second):
  '''Returns the edit distance between  the strings first and second.'''

  # if the first string is empty, we can do len(second) deletions
  if not first:
    return len(second)

  # if the second string is empty, we can do len(first) insertions
  elif not second:
    return len(first)

  # if the first characters of each string agrees, then we don't need to
  # perform a transformation for those characters
  elif first[0] == second[0]:
    return editDistance(first[1:], second[1:])

  # if the first characters of the two strings are different, consider 
  # the effects of performing each kind of modification on those characters;
  # choose the option that leads to the cheapest cost
  else:
    substitution = 1 + editDistance(first[1:], second[1:])
    deletion = 1 + editDistance(first[1:], second)
    insertion = 1 + editDistance(first, second[1:])
    return min(substitution, deletion, insertion)

print(editDistance("car", "cate"))
print(editDistance("antidisestablishment", "antiquities"))
print(editDistance("xylophone", "yellow"))
print(editDistance("follow", "yellow"))
print(editDistance("lower", "hover"))