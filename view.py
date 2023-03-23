from tabulate import tabulate


def greetings():
    print('Здравствуйте!')


def menu():
    print('Menu')
    print('1. Показать все контакты.', '\n'
          '2. Добавить контакт.', '\n'
          '3. Найти контакт.', '\n'
          '4. Выход')


def show_phonebook(date):
    print(tabulate(date, headers=['Имя', 'Фамилия', 'Телефон'], tablefmt='grid'))

def ask_find():
    print('Введите значение: ')

def print_finded_line(finded_line):
    print('Найдено: \n', tabulate(finded_line, headers=['Имя', 'Фамилия', 'Телефон'], tablefmt='grid'))