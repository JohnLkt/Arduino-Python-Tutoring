class Contact:
    def __init__(self, Nama, Nomor):
        self.Nama = Nama
        self.Nomor = Nomor

    def display_info (self):
        return f"Nama: {self.Nama}, Phone Number: {self.Nomor}"
    
class Phonebook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, Nama, Nomor):
        contact = Contact(Nama, Nomor)
        self.contacts.append(contact)
        print ("Contact Added Succesfully")

    def del_contact (self, Nama):
        for contact in self.contacts:
            if contact.Nama == Nama:
                self.contacts.remove(contact)
                print ("Contact Deleted Succesfully")

    def search_contact (self, Nama):
        for contact in self.contacts:
            if contact.Nama == Nama:
                print (f"Contact Found! Nama: {contact.Nama}, Phone Number: {contact.Nomor}")

    def display_all_contact (self):
        if not self.contacts:
            print ("No Contacts Found")
        else:
            print ("All Contacts: ")
            for contact in self.contacts:
                print (contact.display_info())

x = Phonebook()

while True:
    print ("\nMenu")
    print ("1. Add Contact")
    print ("2. Delete Contact")
    print ("3. Search Contact")
    print ("4. Display All Contact")
    print ("5. Exit")

    choice  = input ("Enter Number From 1 - 5")

    if choice == '1':
        Nama = input ("Masukan Nama: ")
        Nomor = input ("Masukkan Nomor Telfon: ")
        x.add_contact(Nama, Nomor)

    elif choice == '2':
        Nama = input ("Masukkan Nama Untuk Dihapus: ")
        x.del_contact(Nama) 

    elif choice == '3':
        Nama = input ("Masukkan Nama untuk dicari: ")
        x.search_contact(Nama) 
    
    elif choice == '4':
        x.display_all_contact()
    
    elif choice == '5':
        print ("Exit Phonebook")
        break

    else:
        print ("Angka harus antara 1 - 5")