import time

def time_this(num_runs):
    def decorator(func):
        def wrapper():
            action_time = 0
            for _ in range(num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                action_time += (t1 - t0)
            avg_time = action_time / num_runs
            return avg_time
        return wrapper
    return decorator

@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass
print(f())

