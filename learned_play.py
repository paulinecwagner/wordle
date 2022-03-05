from util import print_
import random
import torch
from IPython import embed
from typing import Callable


class Wordle:
    max_guesses = 3
    word_length = 5

    def __init__(self, solution=None, valid_words=None):
        self.words = valid_words or [l.strip() for l in open("words")]
        self.guess_dim = len(self.words) + 1
        self.words = {
            word: torch.nn.functional.one_hot(torch.tensor(i + 1), self.guess_dim)
            for i, word in enumerate(self.words)
        }
        self.solution = solution or random.choice(list(self.words.keys()))
        invalid_guesses = (
            torch.nn.functional.one_hot(torch.tensor(0), self.guess_dim).repeat(
                self.max_guesses
            )
        ).flatten()
        invalid_reports = torch.tensor([0] * (self.word_length * self.max_guesses))
        self.game_state = torch.cat((invalid_guesses, invalid_reports))
        self.current_guess = 0
        self.done = False

    def evaluate(self, guess: str):
        ans = torch.zeros(self.word_length).long()
        if not guess in self.words:
            print_(f"{guess} is not valid")
            return None
        for i in range(len(guess)):
            if guess[i] in self.solution:
                if guess[i] == self.solution[i]:
                    ans[i] = 2
                else:
                    ans[i] = 1
            else:
                ans[i] = 0
        print_("answer: ", "".join([str(x.item()) for x in ans]))
        return ans


    def update_game_state(self, guess: str, report: str):
        current_guess_idx = (self.current_guess - 1) * self.guess_dim
        next_guess_idx = current_guess_idx + self.guess_dim
        self.game_state[current_guess_idx:next_guess_idx] = self.words[guess]
        current_report_idx = (
            self.guess_dim * self.max_guesses
            + (self.current_guess - 1) * self.word_length
        )
        next_report_idx = current_report_idx + self.word_length
        self.game_state[current_report_idx:next_report_idx] = report

    def make_guess(self, guess):
        if not self.done:
            self.current_guess += 1
            report = self.evaluate(guess)
            self.update_game_state(guess, report)
        if guess == self.solution or self.current_guess >= self.max_guesses:
            self.done = True
        return self.game_state

    def __repr__(self):
      return str(self.game_state)


def random_guess_maker(game: Wordle):
    return random.choice(list(game.words.keys()))


def smart_guess_maker(game: Wordle):
    return game.solution

def get_model(input_dim, output_dim):
  return torch.nn.Sequential(
    torch.nn.Linear(input_dim, 128),
    torch.nn.ReLU(),
    torch.nn.Linear(128, 128),
    torch.nn.ReLU(),
    torch.nn.Linear(128, output_dim)
  )

def play_round(words, decider):
  state_mem = []
  value_mem = []
  rewards = []
  game = Wordle(valid_words = words)
  while not game.done:
      guess = decider(game)
      state = game.make_guess(guess)
      state_mem.append(state)  
      rewards += [game.max_guesses - game.current_guess + 1 if game.done else 0]
  # discounted rewards
  for i in range(len(rewards)):
    value_mem.append(sum([r * (0.9 ** j) for j,r in enumerate(rewards[i:])]))
  return state_mem, value_mem


def train(epochs, words):
  input_dim = (len(words) + 1) * Wordle.max_guesses + Wordle.word_length * Wordle.max_guesses
  value_net = get_model(input_dim, len(words) + 1)
  action_decider = get_model(input_dim, len(words) + 1)
  optimizer = torch.optim.Adam(value_net.parameters(), lr=0.001)
  state_memory = []
  value_memory = []
  for _ in range(10000):
    state_mem, value_mem = play_round(words, random_guess_maker)
    state_memory += state_mem
    value_memory += value_mem

  # TODO trained play


if __name__ == "__main__":
    random.seed(1)
    mini_words = random.sample([l.strip() for l in open("words")], 10)
    train(100, mini_words)
