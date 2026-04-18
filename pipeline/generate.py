import random

def create_predictions(results):

    top = results[:13]
    elite = results[:6]

    return {
        "top13": top,
        "top6": elite
    }
