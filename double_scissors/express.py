import random

import numpy as np


class Human(object):
  def __init__(self):
    self.policy = {
      (0, 0): self.rand_dist(),
      (0, 1): self.rand_dist(),
      (1, 0): self.rand_dist(),
      (1, 1): self.rand_dist()
    }
    self.score = 0
    self.lifespan = 0

  def rand_sum1(self, l):
    l = [abs(x) for x in l]
    total = sum(l)
    return [x / total for x in l]

  def rand_dist(self):
    l = [random.random() for x in range(4)]
    return self.rand_sum1(l)

  def throw(self, state):
    return np.random.choice(range(4), p=self.policy[state])

  def mutate(self):
    h2 = Human()
    policy = {}
    for key, value in self.policy.items():
      v2 = list(value)
      for i in range(len(v2)):
        v2[i] += random.random() * 0.02 - 0.01
      policy[key] = self.rand_sum1(v2)
    h2.policy = policy
    return h2


def win_update(score):
  return score[0] + 1, score[1]


def loss_update(score):
  return score[0], score[1] + 1


def play_game(h1, h2):
  scores = (0, 0)
  while max(scores) < 2:
    t1 = h1.throw(scores)
    t2 = h2.throw(scores[::-1])
    if t1 == ROCK:
      if t2 == SCISSORS or t2 == DOUBLE_SCISSORS:
        scores = win_update(scores)
      if t2 == PAPER:
        scores = loss_update(scores)
    if t1 == PAPER:
      if t2 == ROCK:
        scores = win_update(scores)
      if t2 == SCISSORS:
        scores = loss_update(scores)
      if t2 == DOUBLE_SCISSORS:
        return LOSS
    if t1 == SCISSORS:
      if t2 == PAPER:
        return WIN
      if t2 == DOUBLE_SCISSORS or t2 == ROCK:
        scores = loss_update(scores)
    if t1 == DOUBLE_SCISSORS:
      if t2 == SCISSORS or t2 == PAPER:
        scores = win_update(scores)
      if t2 == ROCK:
        scores = loss_update(scores)
  if scores[0] == 2:
    return WIN
  return LOSS


def out_come(t1, t2, scores):
  if t1 == ROCK:
    if t2 == SCISSORS or t2 == DOUBLE_SCISSORS:
      scores = win_update(scores)
    if t2 == PAPER:
      scores = loss_update(scores)
  if t1 == PAPER:
    if t2 == ROCK:
      scores = win_update(scores)
    if t2 == SCISSORS:
      return (0, 2)
    if t2 == DOUBLE_SCISSORS:
      scores = loss_update(scores)
  if t1 == SCISSORS:
    if t2 == PAPER:
      return (2, 0)
    if t2 == DOUBLE_SCISSORS or t2 == ROCK:
      scores = loss_update(scores)
  if t1 == DOUBLE_SCISSORS:
    if t2 == SCISSORS or t2 == PAPER:
      scores = win_update(scores)
    if t2 == ROCK:
      scores = loss_update(scores)
  return scores


def play_game2(h1, h2, state):
  if max(state) == 2:
    if state[0] == 2:
      return 1.0
    return 0.0
  policy1 = h1.policy[state]
  policy2 = h2.policy[state]
  non_tie_prob = 0
  for t1, p1 in enumerate(policy1):
    for t2, p2 in enumerate(policy2):
      if t1 == t2:
        continue
      non_tie_prob += p1 * p2
  scale_factor = 1.0 / non_tie_prob
  total = 0
  for t1, p1 in enumerate(policy1):
    for t2, p2 in enumerate(policy2):
      if t1 == t2:
        continue
      p_outcome = p1 * p2 * scale_factor
      ex_outcome = play_game2(h1, h2, out_come(t1, t2, state))
      total += p_outcome * ex_outcome
  return total


population_n = 1000
num_rounds = 100000
ROCK = 0
PAPER = 1
SCISSORS = 2
DOUBLE_SCISSORS = 3
WIN = "WIN"
LOSS = "LOSS"

population = [Human() for x in range(population_n)]
for round in range(num_rounds):
  print(round)
  # score humans
  for h in population:
    opponents = random.sample(population, 20)
    for opp in opponents:
      h.score += play_game2(h, opp, (0, 0))

  # Cull half the population
  population = sorted(population, key=lambda x: x.score, reverse=True)
  population = population[:int(population_n / 2)]

  # Replace 1/4 population with mutations
  parents = random.sample(population, int(population_n / 4))
  for parent in parents:
    population.append(parent.mutate())

  # Replace 1/4 population with new participants
  population = population + [Human() for x in range(int(population_n / 4))]

  for elem in population:
    elem.score = 0
    elem.lifespan += 1

  if round % 40 == 39:
    print("LOGGING")
    for h in population:
      opponents = random.sample(population, 100)
      for opp in opponents:
        if h == opp:
          continue
        h.score += play_game2(h, opp, (0, 0))

    population = sorted(population, key=lambda x: x.score, reverse=True)
    print(population[0].score)
    print(population[0].policy)

    print(population[1].score)
    print(population[1].policy)

    print([x.lifespan for x in population[:40]])
    print([x.score for x in population[:40]])
    for elem in population:
      elem.score = 0

print("LOGGING")
for h in population:
  opponents = random.sample(population, 100)
  for opp in opponents:
    if h == opp:
      continue
    h.score += play_game2(h, opp, (0, 0))

population = sorted(population, key=lambda x: x.score, reverse=True)
print(population[0].score)
print(population[0].policy)

print(population[1].score)
print(population[1].policy)

print([x.lifespan for x in population[:40]])
print([x.score for x in population[:40]])
for elem in population:
  elem.score = 0
