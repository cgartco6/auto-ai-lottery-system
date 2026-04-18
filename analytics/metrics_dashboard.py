def build_metrics_report(data):

    return {
        "total_simulations": len(data),
        "unique_combinations": len(set(tuple(x) for x in data))
    }
