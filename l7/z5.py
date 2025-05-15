from z4 import make_generator, fibonacci_rec, fibonacci_iter
from typing import Generator

def make_generator_mem(f: callable) -> Generator[any, None, None]:
    from functools import lru_cache
    from copy import deepcopy
    f_ = deepcopy(f)

    @lru_cache(maxsize=1024)
    def wrapper_(*args, **kwargs):
        return f_(*args, **kwargs)

    print(f_.__globals__[f_.__name__])
    f_.__globals__[f_.__name__] = wrapper_
    #print(f_.__globals__[f_.__name__])
    return make_generator(wrapper_)



# dla 5k
# iter 12s
# rec 9s
def main() -> None:
    mem_gen = make_generator_mem(fibonacci_rec)
    print(type(fibonacci_rec))
    for i, fib in zip(range(500), mem_gen):
        pass
    print(fibonacci_iter.__globals__['fibonacci_rec'])

if __name__ == '__main__':
    main()

# opc param