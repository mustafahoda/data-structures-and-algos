from pdb import  set_trace

def bubble_sort(A: list) -> list:

    sorted = len(A)
    #inner pass


    for i in range(len(A)):

        L = 0
        R = 1

        # set_trace()

        while R != len(A) :

            # set_trace()

            # if L > R, then swap
            if A[L] > A[R]:
                temp = A[L]
                A[L] = A[R]
                A[R] = temp

            L = L + 1
            R = R + 1


    return A

if __name__ == "__main__":
    print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))