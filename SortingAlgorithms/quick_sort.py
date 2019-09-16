def partition(xs, start, end):
    follower = leader = start
    while leader < end:
        if xs[leader] <= xs[end]:
            xs[follower], xs[leader] = xs[leader], xs[follower]
            follower += 1
        leader += 1
    xs[follower], xs[end] = xs[end], xs[follower]
    return follower


def _quicksort(xs, start, end):
    if start >= end:
        return
    p = partition(xs, start, end)
    _quicksort(xs, start, p - 1)
    _quicksort(xs, p + 1, end)

    return xs


def quicksort(xs):
    _quicksort(xs, 0, len(xs) - 1)

    return xs

if __name__ == "__main__":
    A = [7,2,1,6,8,5,3,4]
    B = [4,5,6,2,3,9,10,2,1,5,3,100,23,42,1]
    print(quicksort(B))
    # print(partition(A, 0))