def is_unique(string):
    existing_chars = set()
    for char in string:
        if char not in existing_chars:
            existing_chars.add(char)
        else:
            return False
    return True


def is_permutation(s1, s2):
    f1 = [0] * 128
    f2 = [0] * 128
    for char in s1:
        f1[ord(char)] += 1
    for char in s2:
        f2[ord(char)] += 1
    return f1 == f2


def urlify(string):
    return ''.join(map(lambda x: x if x != ' ' else '%20', string))


def palindrome_permutation(string):
    string = string.lower()
    string = string.replace(' ', '')
    freq = [0] * 128
    for char in string:
        freq[ord(char)] += 1
    num_odd = 0
    for num in freq:
        if num % 2 == 1:
            num_odd += 1
        if num_odd > 1:
            return False
    return True


def one_away(s1, s2):
    # replacement
    if len(s1) == len(s2):
        return sum(map(lambda x: x[0] != x[1], zip(s1, s2))) <= 1
    # deletion / insertion are equivalent
    else:
        longer = s1 if len(s1) > len(s2) else s2
        shorter = s1 if len(s1) < len(s2) else s2
        i, num_away = 0, 0
        while i < len(shorter):
            if i + num_away < len(longer) and shorter[i] != longer[i + num_away]:
                num_away += 1
            else:
                i += 1
        return num_away <= 1


def string_compression(string):
    string += ' '
    new_string = ''
    num_chars = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            num_chars += 1
        else:
            new_string += string[i] + str(num_chars)
            num_chars = 1
    if len(new_string) < len(string) - 1:
        return new_string
    else:
        return string[:-1]  # chop off extra char


def rotate_90(matrix):
    n = len(matrix)
    matrix.reverse()  # swap rows
    for r in range(n):  # transpose
        for c in range(r, n):
            temp = matrix[r][c]
            matrix[r][c] = matrix[c][r]
            matrix[c][r] = temp
    return matrix


def zero_matrix(matrix):
    coords = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                coords.append((r, c))
    for coord in coords:
        matrix[coord[0]] = [0] * len(matrix[coord[0]])  # set row to 0
        for r in range(len(matrix)):
            matrix[r][coord[1]] = 0  # set col to 0
    return matrix


def string_rotation(s1, s2):
    return len(s1) == len(s2) and (s1 + s1).find(s2) >= 0


# print(rotate_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(one_away('valk', 'bvalk'))
print(string_rotation('waterbottle', 'erbottlewat'))
