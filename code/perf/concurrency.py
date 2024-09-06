import concurrent.futures
from time import sleep, time
start_time = time()


def complete_square(n):
    sleep(1)
    return n * n


results = []
# for i in range(5):
#     results.append(complete_square(i))

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(complete_square, range(10)))

end_time = time()
duration = end_time - start_time

print(results)
print(f"duration = {duration}")
