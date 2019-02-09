from functools import wraps, partial
import logging
from random import random
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%H:%M:%S',
                    filename='decorators.log',
                    filemode='a')


def timeit(func):
    '''Decorator to ...'''
    @wraps(func)  # preserves function meta data
    def wrapper(*args, **kwargs):
        # do stuff before func
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print()
        print(f'{func.__name__} of args: {args} took {end-start}')
        return result
        # do stuff after func
    return wrapper


def mute_exception(func=None, *, reraise=False, default_return=None):
    if func is None:
        return partial(mute_exception, reraise=reraise, default_return=default_return)

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logging.debug(f'{func.__name__} called for args {args}')
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f'{func.__name__} raised exception {e.__class__.__name__} for args: {args}')
            if reraise:
                raise
            return default_return
    return wrapper

if __name__ == '__main__':

    @timeit

    @mute_exception(reraise=False, default_return=0)
    def div(i, j):
        time.sleep(random())
        return i/j

    a = (1, 2, 3)
    b = (4, 5, 6)

    for i, j in zip(a, b):
        res = div(i, j)
        print(f'div {i}/{j} = {res}')
