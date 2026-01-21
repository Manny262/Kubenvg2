import os, time

totTime = []
for value in os.environ.get('PATH', '').split(os.pathsep): 
    try:
            start = time.perf_counter()
            os.path.exists(value)
            elapsed = time.perf_counter() - start
            print(f'{value}, time: {elapsed:.6f}s')
            totTime.append(elapsed)
    except OSError:
            print(f"path {value} does not exists, or is not accessible")
print(f'Total time: {sum(totTime):.6}s')