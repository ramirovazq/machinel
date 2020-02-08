import numpy as np
def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success
    n_success = 0

    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = np.random.random()
        print(i, random_number)
        # If less than p, it's a success so add one to n_success
        if random_number < p:
            n_success += 1

    return n_success

if __name__ == "__main__":
    number_success = perform_bernoulli_trials(100, 0.05)
    print(number_success)