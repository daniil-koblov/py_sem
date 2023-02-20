# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, 
# которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека).
# 4. Использование функций. Ваша программа не должна быть линейной/

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


def see():
    data = open('file.txt', 'r', encoding = 'utf-8')
    for i in data:
        print(i)
    data.close()

# see()

def save(strk):
    with open ('file.txt', 'a', encoding = 'utf-8') as data:
        data.writelines(strk + '\n')
        data.close()

# save(input())

def search(strk):
    data = open('file.txt', 'r', encoding = 'utf-8')
    strk = strk.split()
    for i in data:
        for j in i.split():
            if j in strk: print(i)

x = 0
while x != 4:
    x = int(input(':'))
    if x == 1:
        see()
    if x == 2:
        save(input())
    if x == 3:
        search(input())
    if x == 4:
        break