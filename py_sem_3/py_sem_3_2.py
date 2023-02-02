# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

str_0 = [1, 2, 3, 4, 5]
k = int(input('Введите сдвиг: '))

for i in range(k-1):
    str_0.insert(0, str_0[-1])
    str_0.pop()

print(str_0)



# new_str = []
# for i in range(k - 1 % len(str_0)):
#     new_str.insert(0, str_0[-1 - i])

# for i in range(len(str_0) - k - 1 % len(str_0)):
#     new_str.append(str_0[i])
# print(new_str)
