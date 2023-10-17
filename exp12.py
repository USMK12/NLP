class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, sentence):
        chart = [[] for _ in range(len(sentence) + 1)]
        chart[0].append((self.grammar.start, (), 0))

        for i in range(len(sentence) + 1):
            while True:
                added = False
                for state in chart[i]:
                    if not self.is_complete(state):
                        self.predict(chart, i, state)
                    else:
                        self.scan(chart, i, state)
                        self.complete(chart, i, state)
                    added = True
                if not added:
                    break

        return any(state == (self.grammar.start, (), len(sentence)) for state in chart[-1])

    def predict(self, chart, i, state):
        for production in self.grammar.productions:
            if production.lhs == state[0]:
                chart[i].append((production.rhs[0], (), i))

    def scan(self, chart, i, state):
        if i < len(sentence) and sentence[i] == state[0]:
            chart[i + 1].append((state[0], (), i))

    def complete(self, chart, i, state):
        for completed_state in chart[state[2]]:
            if not self.is_complete(completed_state) and completed_state[0] == state[0]:
                chart[i].append((completed_state[0], completed_state[1] + (state,), completed_state[2]))

    def is_complete(self, state):
        return len(state[1]) == len(self.grammar.productions[state[0]])

class Grammar:
    def __init__(self, start, productions):
        self.start = start
        self.productions = productions

sentence = "the cat sat on the mat"
grammar = Grammar(
    start=0,
    productions=[
        (0, ("the",)),
        (1, ("cat",)),
        (2, ("sat",)),
        (3, ("on",)),
        (4, ("mat",)),
        (5, (1, 2)),
        (6, (3, 4)),
        (7, (0, 5)),
        (8, (7, 6)),
    ]
)

parser = EarleyParser(grammar)
print(parser.parse(sentence.split()))
