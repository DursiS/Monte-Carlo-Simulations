import random
import math


def simulate(k: int, _candidates: list[int]) -> int:
    """Add to <dct> k: average payoff.

    Precondition: k > 0
    """
    best_so_far = max(_candidates[:k])
    choice = None

    for candidate in _candidates[k:]:
        if candidate > best_so_far:
            choice = candidate
            break

    return 1 if choice == max(_candidates) else 0


if __name__ == "__main__":
    n = 10000  # Optimizing a permutation of n consecutive numbers
    candidates = list(range(1, n + 1))
    random.shuffle(candidates)

    # Calculate expected payoff
    total_payoff = 0
    for k in range(1, n - 1):
        total_payoff += simulate(k, candidates)
    average_payoff = total_payoff / n

    # Print it
    optimal = round(n / math.exp(1)) / n
    print(f"Got: {average_payoff}; Expected: {optimal}")
