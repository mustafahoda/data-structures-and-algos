# def partition(xs, start, end):
#     follower = leader = start
#     while leader < end:
#         if xs[leader] <= xs[end]:
#             xs[follower], xs[leader] = xs[leader], xs[follower]
#             follower += 1
#         leader += 1
#     xs[follower], xs[end] = xs[end], xs[follower]
#     return follower
#
#
# def _quicksort(xs, start, end):
#     if start >= end:
#         return
#     p = partition(xs, start, end)
#     _quicksort(xs, start, p - 1)
#     _quicksort(xs, p + 1, end)
#
#     return xs
#
#
# def quicksort(xs):
#     _quicksort(xs, 0, len(xs) - 1)
#
#     return xs


from pdb import set_trace

def quicksort(A: list) -> list:

    print("A before partition: %s" % A)

    if len(A) <= 1:
        return A

    pIndex = partition(A)

    print("A after partition: %s" % A)

    set_trace()


    quicksort(A[:pIndex])
    quicksort(A[pIndex + 1:])

    return A

def partition(A):
    pivot = A[-1]

    i = 0
    pIndex = 0

    while i != len(A) - 1:

        # set_trace()

        if pivot > A[i]:
            # implement swap between pIndex and A[i]

            temp = A[i]
            A[i] = A[pIndex]
            A[pIndex] = temp

            pIndex = pIndex + 1

        i = i + 1

    # once we reach the element before the pivot, we swap pivot into pIndex
    temp = A[pIndex]
    A[pIndex] = pivot
    A[-1] = temp

    return pIndex

if __name__ == "__main__":
    A = [7,2,1,6,8,5,3,4]
    B = [4,5,6,2,3,9,10,2,1,5,3,100,23,42,1]
    # print(quicksort(B))
    # print(partition(A, 0))
    # print(partition(A))
    print(quicksort(A))