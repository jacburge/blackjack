'''
@timeit decorator which allows you to measure the execution time of the method/function by just adding the @timeit decorator on the method.

Usage:
from common.timeit import timeit

@timeit
def add(a,b):  # your function
    return a+b

Code copied from:
https://medium.com/pythonhive/python-decorator-to-measure-the-execution-time-of-methods-fa04cb6bb36d

This is less code than:

start_time = int(round(time.time() * 1000))
employees = Employee.get_all_employee_details() 
time_diff = current_milli_time() — start_time debug_log_time_diff.update({'FETCH_TIME': time_diff})

'''
import logging
import time

logger = logging.getLogger(__name__)

# TODO How to use log_name and log_time


def timeit(method):
    def timed(*args, **kw):
        start_time = time.time()  # TODO use time.perf_counter()   for more accurate
        result = method(*args, **kw)
        stop_time = time.time()
        print('%r  %2.2f ms' %
              (method.__name__, (stop_time - start_time) * 1000))
        return result
    return timed


def timeit_to_log(method):
    ''' If your code implements a logger, this decorater will log to that logger; otherwise, it 
    will log to stdout.
    '''
    def timed(*args, **kw):
        start_time = time.time()  # TODO use time.perf_counter()   for more accurate
        result = method(*args, **kw)
        stop_time = time.time()
        logger.debug('%r  %2.2f ms' %
                     (method.__name__, (stop_time - start_time) * 1000))
        return result
    return timed
