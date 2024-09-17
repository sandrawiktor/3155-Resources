from human_records.Person import Person
from human_records.Student import Student

jake = Person("Jake", "Wright", "1111111111")
alice = Student("Alice", "Webber", "7187771111", "Sophomore")

people = [jake, alice]

for person in people:
    print(person.say_name())
    print(person.info())
    print("------")