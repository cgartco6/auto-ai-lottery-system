import random

def simulate(n=10000):
    return [sorted(random.sample(range(1,51),5)) for _ in range(n)]
