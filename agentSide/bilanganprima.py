import multiprocessing

# Cek bilangan prima
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Worker mencari bilangan prima
def find_primes(start, end):
    primes = []
    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)
    return primes

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    start = 1
    end = 200
    workers = multiprocessing.cpu_count()

    step = (end - start + 1) // workers
    tasks = []

    for i in range(workers):
        s = start + i * step
        e = start + (i + 1) * step - 1
        if i == workers - 1:
            e = end
        tasks.append((s, e))

    pool = multiprocessing.Pool(workers)
    results = pool.starmap(find_primes, tasks)

    pool.close()
    pool.join()

    # Gabungkan hasil
    all_primes = []
    for r in results:
        all_primes.extend(r)

    # Sorting menggunakan Bubble Sort
    bubble_sort(all_primes)

    print("Bilangan Prima Terurut:")
    print(all_primes)
