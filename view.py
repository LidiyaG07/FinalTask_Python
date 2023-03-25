from tabulate import tabulate


def greetings():
    print('Здравствуйте!')


def menu():
    print('МЕНЮ:')
    print('1. Показать все контакты.', '\n'
          '2. Добавить контакт.', '\n'
          '3. Найти контакт.', '\n'
          '4. Изменить контакт', '\n'
          '5. Удалить контакт', '\n'
          '6. Выход')


def show_phonebook(date):
    print(tabulate(date, headers=['Имя', 'Фамилия', 'Телефон'], tablefmt='grid'))

def ask_find():
    print('Введите контакт: ')

def print_finded_line(finded_line):
    print('Найдено: \n', tabulate(finded_line, headers=['Имя', 'Фамилия', 'Телефон'], tablefmt='grid'))

def menu_of_change_contact():
    print('\nМеню:\n1. Изменить имя\n2. Изменить фамилию\n3. Изменить номер телефона\n4. Выход')