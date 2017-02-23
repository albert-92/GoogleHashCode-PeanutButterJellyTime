from simanneal import Annealer


class ChallengeProblem(Annealer):

    def __init__(self, state, data):
        self.data = data
        super(ChallengeProblem, self).__init__(state)

    def move(self):
        self.state = self.state

    def energy(self):
        return sum(self.state)


initial_state = []
tsp = ChallengeProblem(initial_state)
best_state, best_energy = tsp.anneal()