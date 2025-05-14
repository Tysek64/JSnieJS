def forall(pred, iterable):
    return not atleast(lambda x: not pred(x), iterable, 1)

def exists(pred, iterable):
    return atleast(pred, iterable, 1)

def atleast(pred, iterable, n):
    sum = 0
    for elem in iterable:
        if pred(elem):
            sum += 1
        if sum >= n:
            return True
    return False

def atmost(pred, iterable, n):
    return not atleast(pred, iterable, n + 1)

if __name__ == '__main__':
    print(forall(lambda x: x % 2 == 0, [2, 4, 5, 8]))
    print(forall(lambda x: x % 2 == 0, [2, 4, 6, 8]))

    print(exists(lambda x: x % 2 == 0, [1, 3, 5, 7]))
    print(exists(lambda x: x % 2 == 0, [2, 4, 5, 8]))

    print(atleast(lambda x: x % 2 == 0, [2, 4, 5, 7], 3))
    print(atleast(lambda x: x % 2 == 0, [2, 4, 5, 8], 3))

    print(atmost(lambda x: x % 2 == 0, [2, 4, 5, 8], 2))
    print(atmost(lambda x: x % 2 == 0, [2, 4, 5, 7], 2))

    import itertools

    print(forall(lambda x: x % 2 == 0, itertools.count(1)))
    print(exists(lambda x: x % 2 == 0, itertools.count(1)))
    print(atmost(lambda x: x % 2 == 0, itertools.count(1), 5))
    print(atleast(lambda x: x % 2 == 0, itertools.count(1), 5))
    print(forall(lambda x: x % 2 == 0, itertools.count(2, 2)))
