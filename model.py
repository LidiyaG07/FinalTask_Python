
def read_phonebook():
    temp = []
    file = open('file.txt', 'r', encoding='utf-8')
    for line in file.read().split('\n'):
        temp.append(line)
    file.close()
    list_list = []
    for i in temp:
        a = i.split()
        list_list.append(a)
    return list_list[:len(list_list)-1]

def add_contact(first_name, last_name, phone):
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(first_name + ' ' + last_name + ' ' + phone + '\n')
        file.close()


def find(sub_string):
   data = read_phonebook()
   result = []
   for line in data:
       if sub_string in line:
           result.append(line)
   return (result)

def rewrite_line(initinal_line, new_line):
    data = read_phonebook()
    result = []
    for line in data:
        if line == initinal_line:
            result.append(new_line)
        else:
            result.append(line)
    with open('file.txt', 'w', encoding='utf-8') as file:
        for line in result:
            for item in line:
                file.write(item + ' ')
            file.write('\n')
        file.close()

def delete_contact(contact_to_delete):
    data = read_phonebook()
    result = []
    for line in data:
        if line != contact_to_delete:
            result.append(line)
    with open('file.txt', 'w', encoding='utf-8') as file:
        for line in result:
            for item in line:
                file.write(item + ' ')
            file.write('\n')
        file.close()