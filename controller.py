import model
import view

def run():
    view.greetings()
    while True:
        view.menu()
        answer = input('Ответ: ')
        if answer == '1':
            date = model.read_phonebook()
            view.show_phonebook(date)

        elif answer == '2':
            first_name = input('Введите имя: ')
            last_name = input('Введите фамилию: ')
            phone = input('Введите номер телефона: ')
            model.add_contact(first_name, last_name, phone)


        elif answer == '3':
            view.ask_find()
            sub_string = input()
            finded_line = model.find(sub_string)
            if (finded_line):
                view.print_finded_line(finded_line)
            else:
                print('Не найдено.')

        elif answer == '4':
            print('Изменить контакт: ')
            sub_string = input()
            finded_line = model.find(sub_string)
            if (finded_line):
                if (len(finded_line) > 1):
                    view.print_finded_line(finded_line)
                    input('Введите контакт, который нужно изменить')
