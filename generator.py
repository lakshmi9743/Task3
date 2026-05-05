import random

class MarkovChainTextGenerator:
    def __init__(self, state_size=2):
        self.state_size = state_size
        self.transitions = {}
        self.words = []

    def train(self, text):
        self.words = text.strip().split()
        if len(self.words) < self.state_size:
            raise ValueError("Training text is too short for the selected state size.")

        self.transitions = {}
        for i in range(len(self.words) - self.state_size):
            state = tuple(self.words[i : i + self.state_size])
            next_word = self.words[i + self.state_size]

            if state not in self.transitions:
                self.transitions[state] = []
            self.transitions[state].append(next_word)

    def generate(self, num_words=50, seed_text=None):
        if not self.transitions:
            return "Please train the model with some text first!"

        if seed_text:
            seed_words = seed_text.strip().split()
            if len(seed_words) >= self.state_size:
                current_state = tuple(seed_words[-self.state_size:])
            else:
                current_state = random.choice(list(self.transitions.keys()))
        else:
            current_state = random.choice(list(self.transitions.keys()))

        output = list(current_state)

        for _ in range(num_words - self.state_size):
            if current_state in self.transitions:
                next_word = random.choice(self.transitions[current_state])
                output.append(next_word)
                current_state = tuple(output[-self.state_size:])
            else:
                current_state = random.choice(list(self.transitions.keys()))
                output.extend(list(current_state))

        return " ".join(output[:num_words])