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


def add():
    with open('file.txt', 'a') as data:
        surname = data.write(input('Введите фамилия: '))
        data.write(' ')
        name = data.write(input('Введите имя: '))
        data.write(' ')
        secondname = data.write(input('Введите отчество: '))
        data.write(' ')
        phonenumber = data.write(input('Введите номер телефона: '))
        data.write('\n')
    
def output():
    path = 'file.txt'
    data = open('file.txt', 'r')
    for line in data:
        print(line)
    data.close()

def search(info):
    path = 'file.txt'
    data = open('file.txt', 'r')

    for line in data.readlines():
        if info in line: print(line)
    data.close()

print('Это программа для работы со справочником.\n'
        'Введите 1 для добавления нового абонента.\n'
        'Введите 2 для выведения всех абонентов.\n'
        'Введите 3 для поиска абонента.\n'
        'Введите 4 для завершения работы программы.')
x = 0
while x != 4:
    x = int(input('Введите выбранный вариант: '))
    if x == 1: add()
    elif x == 2: output()
    elif x == 3: search(input('Введите искомую информацию: '))  
    elif x == 4: break