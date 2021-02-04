users_data_science = {12, 45, 56, 78, 90, 13, 46, 87, 53}
users_machine_learning = {12, 34, 67, 83, 45, 90, 98, 87, 12}

print(f"ml: {users_machine_learning}, ds: {users_data_science}")

intersection = users_data_science & users_machine_learning
unity = users_data_science | users_machine_learning
difference_ds = users_data_science - users_machine_learning
difference_ml = users_machine_learning - users_data_science
or_exclusive = users_data_science ^ users_machine_learning

users_data_science.add(35)
users_machine_learning.add(78)
print("Números 35 e 78 add...\n")
print(f"ml: {users_machine_learning}, ds: {users_data_science}\n")
print(f"união: {unity}")
print(f"interseção: {intersection}")
print(f"tem ml nao ds: {difference_ml}")
print(f"tem ds nao ml: {difference_ds}")

test = frozenset({13, 34, 56, 78, 90})
test.add(45)
