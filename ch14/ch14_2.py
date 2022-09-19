import random
import tqdm
from scratch.gradient_descent import gradient_step
from scratch.statistics import num_friends_good, daily_minutes_good
from ch14_1 import error, sum_of_sqerrors


num_epochs = 10000
random.seed(0)

guess = [random.random(), random.random()]

learning_rate = 0.00001        # темп усвоения

with tqdm.trange(num_epochs) as t:
    for _ in t:
        alpha, beta = guess

        # частная производная потери по отношению к alpha
        grad_a = sum(2 * error(alpha, beta, x_i, y_i)
                     for x_i, y_i in zip(num_friends_good,
                                         daily_minutes_good))

        # частная производная потери по отношению к beta
        grad_b = sum(2 * error(alpha, beta, x_i, y_i) * x_i
                     for x_i, y_i in zip(num_friends_good, daily_minutes_good))

        # вычислить потерю для вставки в описание tqdm
        loss = sum_of_sqerrors(alpha, beta, num_friends_good, daily_minutes_good)
        t.set_description(f"потеря: {loss: .3f}")

        # В заключение обновить догадку
        guess = gradient_step(guess, [grad_a, grad_b], -learning_rate)

print(guess)
alpha, beta = guess
assert 22.9 < alpha < 23.0
assert 0.9 < beta < 0.905

