import array as arr
import numpy as np

number = arr.array('d', [1, 3.5])

numbers = np.array([1, 3.5])

print(numbers + 3)

#### Outras Bult-in ####

ages = [12, 45, 24, 59, 10, 34, 12, 18, 35, 23]

for i in range(len(ages)):
    print(i, "->", ages[i])

for index, age in enumerate(ages):
    print(index, ":", age)

users = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for name, age, birth in users:
    print(name)

for _, age, _ in users:
    print(age)