'''
# Contact Class
class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.addr = addr

    def print_info(self):
        print('name :', self.name)
        print('phone_number :', self.phone_number)
        print('email :', self.email)
        print('addr :', self.addr)

# function
def set_content():
    name = input('Name : ')
    phone_number = input('phone number : ')
    email = input('email : ')
    addr = input('addr : ')

    contact = Contact(name, phone_number, email, addr)
    return contact

def print_menu():
    menu = input('select menu no : ')
    return int(menu)

def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

def store_contact(contact_list):
    f = open('contact_db.txt', 'wt')

    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.email + '\n')
        f.write(contact.addr + '\n')

    f.close()

def load_content(contact_list):
    f = open('contact_db.txt', 'rt')

    lines = f.readlines()

    num = len(lines) / 4
    num = int(num)

    for i in range(num):
        name = lines[i * 4].rstrip('\n')
        phone = lines[i * 4 + 1].rstrip('\n')
        email = lines[i * 4 + 2].rstrip('\n')
        addr = lines[i * 4 + 3].rstrip('\n')

        contact = Contact(name, phone, email, addr)

        contact_list.append(contact)

    f.close()
'''

from neural_network import NeuralNetwork


def run():
    print('hello python')

    # set neural network
    input_nodes = 3
    hidden_nodes = 3
    output_nodes = 3
    learning_rate = 0.3

    n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    print('n', n)

    '''
    # set_content()

    contact_list = []
    load_content(contact_list)

    while 1:
        menu = print_menu()

        if menu == 1:
            contact = set_content()
            contact_list.append(contact)

        elif menu == 2:
            print_contact(contact_list)

        elif menu == 3:
            name = input('name : ')
            delete_contact(contact_list, name)

        elif menu == 4:
            store_contact(contact_list)
            break'''


# implementation
if __name__ == '__main__':
    run()
