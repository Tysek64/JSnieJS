from z4 import make_generator, fibonacci_rec, fibonacci_iter
from typing import Generator

def make_generator_mem(f: callable) -> Generator[any, None, None]:
    from functools import lru_cache
    from copy import deepcopy
    f_ = deepcopy(f)

    @lru_cache(maxsize=1024)
    def wrapper_(*args, **kwargs):
        return f_(*args, **kwargs)

    bind_name = f'{f.__name__}_wrapper'
    f_.__globals__[bind_name] = wrapper_

    co_names = list(f.__code__.co_names)
    try:
        co_names[co_names.index(f.__name__)] = bind_name
    except:
        pass
    co_names = tuple(co_names)

    f.__code__ = f.__code__.replace(co_names=co_names)
    #print(f_.__globals__[f_.__name__])
    #print('fv', __test.__code__.co_freevars, __test.__closure__.cell_contents)
    return make_generator(wrapper_)



# dla 5k
# iter 12s
# rec 9s
def main() -> None:
    mem_gen = make_generator_mem(fibonacci_rec)
    #print(type(fibonacci_rec))
    for i, fib in zip(range(5000), mem_gen):
        print(f'{i}: {fib}')
    #print(fibonacci_iter.__globals__['fibonacci_rec'])
    #print(make_generator_mem.__closure__.)

if __name__ == '__main__':
    main()

# opc param