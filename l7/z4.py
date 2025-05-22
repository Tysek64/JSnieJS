from typing import Generator

def make_generator(f: callable) -> Generator[any, None, None]:
    n_seq = 1
    def generator_(): # to jest funkcja zwracajaca generator, ona generuje generator
        nonlocal n_seq
        while True:
            yield f(n_seq)
            n_seq += 1

    return generator_() # to jest generator

def fibonacci_iter(n):
    a, b, c = 0, 1, 0
    for i in range(n):
        c = a
        a = a + b
        b = c
    return a

def fibonacci_rec(n):
    if n < 2:
        return 1
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)


def main() -> None:
    geometric = lambda n: 0.5 ** n

    print("FIBONACCI")
    generator = make_generator(fibonacci_rec)
    for i, fib in zip(range(10), generator):
        print(i, ': ', fib)

    print("GEOMETRIC")
    generator = make_generator(geometric)
    for i, geo in zip(range(10), generator):
        print(i, ': ', geo)



if __name__ == '__main__':
    main()
