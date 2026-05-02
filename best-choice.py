import random
import math


def simulate(k: int, payoffs: dict[int, float], _candidates: list[int]) -> None:
    """Add to <dct> k: average payoff.

    Precondition: k > 0
    """
    best_so_far = max(_candidates[:k])
    choice = None

    for candidate in _candidates[k:]:
        if candidate > best_so_far:
            choice = candidate
            break

    if choice == max(_candidates):
        payoff = 1
    else:
        payoff = 0

    payoffs[k] = payoff
    simulations += 1


def get_optimal_k(payoffs: dict[int, float], _n: int) -> float:
    """Find which key k in <dct> gives the highest average payoff

    Precondition: <dct> is non-empty mapping positive integers to integers.
    """

    total = 0
    for k in list(payoffs.keys()):
        total += payoffs[k]
    return total // n


if __name__ == "__main__":
    n = 1000  # Optimizing a permutation of
    candidates = list(range(1, n + 1))
    random.shuffle(candidates)
    k_payoff_dct = {}

    for k in range(1, n - 1):
        simulate(k, k_payoff_dct, candidates)

    print(k_payoff_dct)
    optimal = round(n / math.exp(1))
    print(f"Got: {get_optimal_k(k_payoff_dct, n)}; Expected: {optimal}")
