import sqlite3


class PhoneBook:

    def __init__(self, number=None, name=None, group=None):
        self.con = sqlite3.connect("contacts.s3db")
        self.cur = self.con.cursor()
        self.number = number
        self.name = name
        self.group = group

    def database(self):
        try:
            self.cur.execute("CREATE TABLE contacts ("
                             "name TEXT,"
                             "number TEXT"
                             ")")
            self.con.commit()
            self.menu()
        except sqlite3.OperationalError:
            self.menu()

    def menu(self):
        print("1. All contacts")
        print("2. Add contact")
        print("3. Remove contact")
        print("4. Exit")

        choice = input("Enter a valid menu: ")
        if choice == '1':
            self.all_contacts()
        elif choice == '2':
            self.add()
        elif choice == '3':
            self.remove()
        elif choice == '4':
            quit()

    def all_contacts(self):
        self.cur.execute("SELECT * FROM contacts")

        if self.cur.fetchall():
            self.cur.execute("SELECT * FROM contacts")
            print()
            for x, contact in enumerate(self.cur.fetchall()):
                print(f'{x+1}. {contact[0]} - {contact[1]}')
            print()
        else:
            print("No contacts saved!\n")

        self.menu()

    def add(self):
        name = input("Enter contact name   : ")
        number = input("Enter contact number : ")

        self.cur.execute("INSERT INTO contacts (name, number) "
                         "VALUES (?, ?)", (name, number))
        self.con.commit()

        print("Contact added successfully!\n")
        self.menu()

    def remove(self):
        number = input("Enter contact number: ")
        self.cur.execute("DELETE FROM contacts "
                         "WHERE number = ?", (number,))
        self.con.commit()

        print("Contact successfully removed!\n")
        self.menu()


PhoneBook().database()
