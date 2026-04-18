from models.monte_carlo import monte_carlo

def run_simulation():

    print("Running simulations...")

    return monte_carlo([0.02]*50, 500000)
