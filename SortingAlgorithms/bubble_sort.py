

def bubble_sort(A: list) -> list:

    sorted = len(A)

    for i in range(len(A)):

        L = 0
        R = 1

        while R != len(A) :

            # if L > R, then swap
            if A[L] > A[R]:
                temp = A[L]
                A[L] = A[R]
                A[R] = temp

            L = L + 1
            R = R + 1


    return A

# def test_benchmark(benchmark):
#     result = bubble_sort([5,2,3,1,6,10,7,8])
#
# test_benchmark(benchmark)
# if __name__ == "__main__":
