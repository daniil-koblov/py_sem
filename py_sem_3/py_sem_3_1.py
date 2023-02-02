# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

str_0 = [1, 4, 2, 0, -1, 3, 4, 1]

new_set = set(str_0)
print(new_set)
print(len(new_set))

# или

print(len(set(str_0)))