def InsertionSort(A):
    assignCount = 0
    for i in range(1, len(A)):
        v = A[i]
        assignCount += 1
        j = i - 1
        while j >= 0 and v < A[j]:
            A[j + 1] = A[j]
            assignCount += 1
            j = j - 1
        A[j + 1] = v
        assignCount += 1
    print("assign count: ", assignCount)

def test():
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    InsertionSort(A)
    print(A)

test()