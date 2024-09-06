from memory_profiler import profile
from time import sleep

import tracemalloc
tracemalloc.start()


@profile
def expensive_function():
    a = [i for i in range(100000)]
    sleep(1)


expensive_function()


snapshot = tracemalloc.take_snapshot()
top_memory_cons = snapshot.statistics("lineno")


print(top_memory_cons)
