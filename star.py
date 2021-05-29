import random

class star:

    def __init__(self, type):
        self.type = type
        if type == 'blue':
            self.size = random.randrange(65, 80)
        elif type == 'white':
            self.size = random.randrange(52, 60) if random.randrange(2) else random.randrange(28, 30)
        elif type == 'yellow':
            self.size = random.randrange(42, 48)
        elif type == 'orange':
            self.size = random.randrange(32, 38)
        elif type == 'red':
            self.size = random.randrange(25, 30) if random.randrange(2) else random.randrange(75, 80)
        self.coordinates = [0, 0]
        self.planets = []

    def __repr__(self):
        return '<r: ' + str(self.size) + ', t: ' + str(self.type) + ', ' + str(self.coordinates) + '>'
