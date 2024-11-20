import random

total_rolls = 0
good_rolls = 0

for rep in range(1000000):  # Use a different variable to avoid overwriting 'i'
    results = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }
    for roll in range(5):  # Roll the dice 5 times
        current = random.randint(1, 6)
        results[current] += 1
    if results[3] > 0 and results[4] > 0 and results[5] > 0:  # Check for 3, 4, and 5
        good_rolls += 1
    total_rolls += 1

all_three_probability = good_rolls / total_rolls

print("Good rolls:", good_rolls)
print("Probability of getting 3, 4, and 5:", all_three_probability)
print("Probability of NOT getting 3, 4, and 5:", 1-all_three_probability)
