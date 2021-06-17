def SelSort(A):
    swapCount = 0
    for i in range(len(A) - 1):
        min = i        
        for j in range(i + 1, len(A)):
                if A[j] < A[min]:
                    min = j
        swapCount += 1
        A[i], A[min] = A[min], A[i]
    print('Swap count is:', swapCount)
                    
def test():
    A = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    SelSort(A)    
    print(A)

test()