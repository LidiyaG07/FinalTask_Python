def read_phonebook():
    with open('file_name.txt', 'r', encoding='utf-8') as file:
        pass

    return None


def add_contact():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    file = open('file.txt', 'a')
    file.write(first_name + ' ')
    file.write(last_name + ' ')
    file.write(phone + '\n')
    file.write('\n')
    file.close()
    return None


def find():

    return None

