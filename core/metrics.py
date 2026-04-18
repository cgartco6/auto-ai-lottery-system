import time

class MetricsTracker:

    def __init__(self):
        self.start_time = time.time()
        self.steps = {}

    def mark(self, step_name):
        self.steps[step_name] = time.time()

    def report(self):
        return {
            "runtime": time.time() - self.start_time,
            "steps": self.steps
        }
