def quicksort(A: list) -> list:
    return _quicksort(A, 0, len(A) - 1)

def _quicksort(A: list, start: int, end: int) -> list:


    if start >= end:
        return A

    print("A before partition: %s" % A)
    pIndex = partition(A, start, end)
    print("A after partition: %s" % A)
    print("_____________________________")



    _quicksort(A, start, pIndex - 1)
    _quicksort(A, pIndex, end)

    return A

def partition(A, start: int, end: int):

    # set_trace()

    pivot = A[end]

    i = start
    pIndex = start

    # set_trace()

    while i < end:

        # set_trace()

        if pivot >= A[i]:

            # implement swap between pIndex and A[i]

            temp = A[i]
            A[i] = A[pIndex]
            A[pIndex] = temp

            pIndex = pIndex + 1

        i = i + 1

    # once we reach the element before the pivot, we swap pivot into pIndex
    temp = A[pIndex]
    A[pIndex] = pivot
    A[end] = temp

    # set_trace()
    print(A)
    return pIndex

if __name__ == "__main__":
    A = [7,2,1,6,8,5,3,4]
    B = [4,5,6,2,3,9,10,2,1,5,3,100,23,42,1]
    C = [7,2,3,8,4]
    D = [2,3]
    # print(quicksort(B))
    # print(partition(A, 0))
    # print(partition(A))
    print(quicksort(B))
    # print(partition(D, 0, 1))