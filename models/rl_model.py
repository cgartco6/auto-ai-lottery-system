import random

class Agent:

    def act(self):

        return sorted(random.sample(range(1,51),5))
