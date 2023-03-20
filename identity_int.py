
num_1 = 1000
num_2 = 1000

print(num_1 == num_2) # Test whether num_1 and num_2 are equal
print(num_1 is num_2) # Test whether num_1 and num_2 refer to the same object
num_1 = num_2 # Now num_1 and num_2 refer to the same object
print(num_1 is num_2)
num_2 = -89 # Make num_2 refer to a different object
print(num_1 is num_2)