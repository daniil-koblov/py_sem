num = int(input('Введите число: '))
fakt = 1
while num > 1:
    fakt *= num
    num -= 1
print(f'Факториал равен {fakt}.')

fact = 1
for i in range(1, num + 1):
    fact *= i 
print(f'Факториал равен {fact}.')