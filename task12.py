class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        contact = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite
        }
        Contacts.current_id += 1
        self.contacts.append(contact)  
                
contacts = Contacts()  # Створення екземпляру класу Contacts
contacts.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)  # Виклик методу add_contacts через екземпляр
print(contacts.list_contacts())         