def generate(results):
    return {
        "top13": results[:13],
        "top6": results[:6]
    }
