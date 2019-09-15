from pdb import set_trace

def shift_items_to_right(B, start, stop):
    for i in range(stop, start, -1):
        B[i] = B[i - 1]

    return B


def insertion_sort(A : list) -> list:
    sorted = 0

    while sorted != len(A):

        hole = 0

        for i in A[:sorted + 1]:
            value = A[sorted]

            if value < A[hole]:
                # move all items to the right from the hole onwards
                shift_items_to_right(A, hole, sorted)

                # store the value in the hole
                A[hole] = value

            else:
                hole = hole + 1

        sorted = sorted + 1

    return A

if __name__ == "__main__":
    print(insertion_sort([12, 11, 13, 5, 6] ))
    # print(shift_items_to_right([2,4,7,1], 0, 3))
