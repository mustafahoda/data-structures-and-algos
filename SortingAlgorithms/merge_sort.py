from pdb import set_trace

def merge(A: list, B: list) -> list:
    ptr_A = 0
    ptr_B = 0

    C = []

    while ptr_A <= len(A) - 1 and ptr_B <= len(B) - 1:

        if A[ptr_A] >= B[ptr_B]:
            C.append(B[ptr_B])
            ptr_B = ptr_B + 1
        else:
            C.append(A[ptr_A])
            ptr_A = ptr_A + 1


    if ptr_A == len(A):
        for i in B[ptr_B:]:
            C.append(i)
    else:
        for i in A[ptr_A:]:
            C.append(i)

    return C

def merge_sort(A: list) -> list:
    print("A: %s" % A)
    if len(A) == 1:
        return A

    # STEP 1: Divide

    mid = len(A) // 2
    L = A[:mid]
    R = A[mid:]
    print("L: %s" % L)
    print("R: %s" % R)


    # set_trace()
    if L is not None:
        L = merge_sort(L)


    if R is not None:
        R = merge_sort(R)


    merged = merge(L, R)
    set_trace()

    print("Merged: %s" % merged)
    return merged

if __name__ == "__main__":
    # print(merge([2], [4,7]))
    # print(merge_sort([2,7,4,1,5,3]))
    print(merge_sort([12, 11, 13, 5, 6, 7]  ))