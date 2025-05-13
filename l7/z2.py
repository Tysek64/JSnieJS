def forall(pred, iterable):
    return sum([pred(elem) for elem in iterable]) == len(iterable)

def exists(pred, iterable):
    return sum([pred(elem) for elem in iterable]) > 0

def atleast(pred, iterable, n):
    return sum([pred(elem) for elem in iterable]) >= n

def atmost(pred, iterable, n):
    return sum([pred(elem) for elem in iterable]) <= n

if __name__ == '__main__':
    print(forall(lambda x: x % 2 == 0, [2, 4, 5, 8]))
    print(forall(lambda x: x % 2 == 0, [2, 4, 6, 8]))

    print()

    print(exists(lambda x: x % 2 == 0, [1, 3, 5, 7]))
    print(exists(lambda x: x % 2 == 0, [2, 4, 5, 8]))

    print()

    print(atleast(lambda x: x % 2 == 0, [2, 4, 5, 7], 3))
    print(atleast(lambda x: x % 2 == 0, [2, 4, 5, 8], 3))

    print()

    print(atmost(lambda x: x % 2 == 0, [2, 4, 5, 8], 2))
    print(atmost(lambda x: x % 2 == 0, [2, 4, 5, 7], 2))
