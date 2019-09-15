from pdb import set_trace

def find_min_not_in_place(A: list, visited) -> int:

    for i in A:
        if visited[i] == False:
            min = i
            break

    for i in A[1:]:
        # set_trace()
        if i < min and visited[i] == False:
            # set_trace()

            min = i
            # visited[min] = True


    return min


def selection_sort_not_in_place(A: list) -> list:

    B = []

    # construct a dictionary that will keep track of visited numbers
    visited = dict()
    for i in A:
        visited[i] = False


    # keep repeating the process until theere are no values in dictionary with False
    while False in visited.values():
        for i in A:

            min = find_min_not_in_place(A, visited)
            # set_trace()
            B.append(min)
            visited[min] = True
            print(B)

    return B

def find_min_in_place(A: list, sorted_index: int) -> int:
    min_index = sorted_index
    min = A[sorted_index]

    # for i in A[sorted_index:]:
    for i in range(sorted_index, len(A)):
        if A[i] < min:
            min = A[i]
            min_index = i


    return (min, min_index)



def selection_sort_in_place(A: list) -> list:

    sorted = 0

    while sorted != len(A):

        # min, min_index = find_min_in_place(A[sorted + 1:])
        min, min_index = find_min_in_place(A, sorted)

        # implement swapping
        temp = A[sorted]
        A[sorted] = min
        A[min_index] = temp

        sorted = sorted + 1

    return A

if __name__ == "__main__":
    # print(selection_sort_not_in_place([64, 25, 12, 22, 11]))
    # visited =  {2: True,
    #             7: False,
    #             4: False,
    #             1: True,
    #             5: False,
    #             3: False,
    #             }
    # print(find_min([2, 7, 4, 1, 5, 3], visited))

    print(selection_sort_in_place([2, 7, 4, 1, 5, 3]))