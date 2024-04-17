class Person:
    def __init__(self, name, company, address, zipcode, phones, email):
        self.name = name
        self.company = company
        self.address = address
        self.zipcode = zipcode
        self.phones = phones
        self.email = email

    def __str__(self):
        return (
            "{}\n"
            "\tCompany: {}\n"
            "\tAddress: {}\n"
            "\tZipcode: {}\n"
            "\tPhones: {}\n"
            "\tEmail: {}"
        ).format(self.name, self.company, self.address, self.zipcode, self.phones, self.email)

with open("address.txt", "r") as file:
    lines = file.readlines()

people = []
for line in lines:
    data = line.strip().split('|')
    people.append(Person(data[0], data[1], data[2], data[3], data[4], data[5]))

print("이름 순 정렬")
people.sort(key=lambda x: x.name)
for pp in people:
    print(pp)

print("\n주소 순 정렬")
people.sort(key=lambda x: x.address)
for pp in people:
    print(pp)
