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
            sub_string = input('Введите контакт, который хотите изменить: ')
            finded_line = model.find(sub_string)
            if (finded_line):
                if (len(finded_line) > 1):
                    view.print_finded_line(finded_line)
                    number_of_contact = int(input())
                else:
                    number_of_contact = 1
                view.print_finded_line(
                    [finded_line[number_of_contact - 1]])
                view.menu_of_change_contact()
                answer_menu = int(input())
                if answer_menu == 1:
                    first_name = input('Введите имя: ')
                    new_line = []
                    new_line.append(first_name)
                    new_line.append(finded_line[number_of_contact - 1][1])
                    new_line.append(finded_line[number_of_contact - 1][2])
                    model.rewrite_line(
                        finded_line[number_of_contact - 1], new_line)
                if answer_menu == 2:
                    first_name = input('Введите фамилию: ')
                    new_line = []
                    new_line.append(finded_line[number_of_contact - 1][0])
                    new_line.append(first_name)
                    new_line.append(finded_line[number_of_contact - 1][2])
                    model.rewrite_line(
                        finded_line[number_of_contact - 1], new_line)
                if answer_menu == 3:
                    phone = input('Введите номер телефона: ')
                    new_line = []
                    new_line.append(finded_line[number_of_contact - 1][0])
                    new_line.append(finded_line[number_of_contact - 1][1])
                    new_line.append(phone)
                    model.rewrite_line(
                        finded_line[number_of_contact - 1], new_line)
                if answer_menu == 4:
                    pass
            else:
                print('Контакт не найден!')


        elif answer == '5':
            sub_string = input('Введите контакт, который хотите удалить: ')
            finded_line = model.find(sub_string)
            view.print_finded_line(finded_line)
            model.delete_contact(finded_line[-1])


        elif answer == '6':
            break