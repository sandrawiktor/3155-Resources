from human_records.Person import Person

class Student(Person):

    def __init__(self, first_name, last_name, phone_number, class_standing):
        super().__init__(first_name, last_name, phone_number)
        self.class_standing = class_standing

    def info(self):
        return(f"{self.first_name}'s phone number is {self.phone_number}.\n" 
              f"{self.first_name}'s class standing is {self.class_standing}")