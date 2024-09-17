class Person:

    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def say_name(self):
        return "Hello, my name is " + self.first_name + " " + self.last_name

    def info(self):
        return f"{self.first_name} phone number is {self.phone_number}"