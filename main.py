from collections import UserDict

class IDException(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value or not value.strip():
            raise ValueError("Name cannot be empty.")
        super().__init__(value)

class Phone(Field):
    def validate(self, phone):
        return len(phone) == 10 and phone.isdigit()

    def __init__(self, value):
        if self.validate(value):
            super().__init__(value)
        else:
            raise ValueError

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if phone is not None:
            new_phone = Phone(phone)
            new_phone.validate(phone)
            if new_phone.value in self.phones:
                self.phones.append(new_phone)

    def remove_phone(self, phone):
        if any(p.value == phone for p in self.phones):
            self.phones = [p for p in self.phones if p.value != phone]
        else:
            raise ValueError(f"Phone {phone} not found in record.")

    def edit_phone(self, old_phone, new_phone):
        if any(p.value == old_phone for p in self.phones):
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
            raise ValueError(f"Phone {old_phone} not found in record.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

