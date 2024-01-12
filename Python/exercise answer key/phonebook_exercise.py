# make a simple phonebook console application using OOP concepts

phone_book = []

class contact_data():
    def __init__(self, a, b, c, d):
        self.Name = a
        self.Address = b
        self.Phone = c
        self.Email = d

    def display_data(self):
        print("Name: " + self.Name)
        print("Address: " + self.Address)
        print("Phone: " + self.Phone)
        print("Email: " + self.Email)

def display_menu():

    print('==================================================')
    print('Welcome to PhoneBook Menu')
    print('1 to add contacts')
    print('2 to display contacts')
    print('press anything else to exit program')
    print('==================================================')
    print('Your Input:')
    menu_input = int(input())

    return menu_input;

def add_contact():
    Name = input('Contact Name: ')
    Address = input('Contact Address: ')
    Phone = input('Contact Phone: ')
    Email = input('Contact Email: ')


    phone_book.append(contact_data(Name, Address, Phone, Email))

    print('==================================================')
    print('1 to add more contacts')
    print('0 to quit to menu')
    add_input = int(input())

    if add_input == 1:
        add_contact()
    elif add_input == 0:
        print('Returning to menu')
    else:
        print('Invalid input, returning to menu')

def display_contact():
    for i in range (0, len(phone_book)):
        print("========================================")
        phone_book[i].display_data()

def main():
    menu_input = display_menu();

    if menu_input == 1:
        add_contact()
        main()
    elif menu_input == 2:
        display_contact()
        main()
    else:
        print('exit')

# start program
main()
