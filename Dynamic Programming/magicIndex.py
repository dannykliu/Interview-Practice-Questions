def magicIndex(A, start, end):
    mid = (start + end) // 2
    print("start", start, "end", end, "mid", mid)
    if A[mid] == mid:  # bc
        return mid
    if start >= end:
        return None  # for tail recursive
    if A[mid] < 0:
        return magicIndex(A, mid + 1, end)
    if A[mid] < mid:  # recursively search right side. search left side from 0 to A[mid]
        # start to A[mid] is first spot a magic index could appear
        return magicIndex(A, mid + 1, end) or magicIndex(A, start, A[mid])
    elif A[mid] > mid:
        return magicIndex(A, start, mid - 1) or magicIndex(A, A[mid], end)


print(magicIndex([1, 3, 4, 5, 6, 7], 0, 5))  # None
print(magicIndex([-2, 1, 4, 5, 6, 8], 0, 5))  # 1
print(magicIndex([-1, -1, 1, 2, 2, 2, 2, 7], 0, 7))  # 7
