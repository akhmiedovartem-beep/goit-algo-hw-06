from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, value):
        if len(value) == 10:
            super().__init__(value)
        else:
            raise ValueError("Phone number must be 10 digits")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, number):
        phone = self.find_phone(number)
        if phone:
            self.phones.remove(phone)


    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
        return None

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)

        if phone:
            phone.value = Phone(new_phone).value
        else:
            raise ValueError("Phone number not found")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        for record in self.data.values():
            if record.name.value == name:
                return record
        return None

    def delete(self, name):
        record  = self.find(name)
        if record:
            del self.data[record.name.value]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())