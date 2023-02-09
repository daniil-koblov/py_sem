# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
import random

number = int(input("Ближайшие к числу: "))
spam = []

def loh(a, b):
    min = b[0]
    for i in range(a):
        b.append(random.randint(1, 5))
        if b[i] < min: min = b[i]
    for i in b:
        b.append(min)
    return b
print(loh(number, spam))
