num = int(input('Введите число: '))
fakt = 1
while num > 1:
    fakt *= num
    num -= 1
print(f'Факториал равен {fakt}.')