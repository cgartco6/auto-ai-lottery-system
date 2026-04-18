from multiprocessing import Pool, cpu_count

def run_parallel(task, data):

    workers = cpu_count()

    with Pool(workers) as pool:
        results = pool.map(task, data)

    return results
