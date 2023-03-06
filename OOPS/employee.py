from datetime import datetime


class Employee:
    # class variable
    no_of_employees = 0
    raise_amount = 1.05

    def __init__(self, name, salary):
        # instance variable
        self.name = name
        self.salary = salary

        Employee.no_of_employees += 1

    @classmethod
    def from_string(cls, data):
        name, salary = data.split("-")
        salary = float(salary)
        return cls(name, salary)

    @classmethod
    def from_list(cls, data):
        name, salary = data
        return cls(name, salary)

    @staticmethod
    def is_holiday(day):
        if day.weekday() in [5, 6]:
            return True
        return False

    def raise_salary(self):
        self.salary = self.salary*Employee.raise_amount

    def display_details(self):
        self.raise_salary()
        print(f"Name: {self.name}, Salary: {self.salary}")


om = Employee("Om", 10000)
ninad = Employee("Ninad", 20000)

# akshit.display_details()
# viral.display_details()

hardik_data = "Hardik-50000"
shruti_data = "Shruti-25000"

hardik = Employee.from_string(hardik_data)
ashwini = Employee.from_string(shruti_data)

tanmay_list_data = ["Tanamy", 50000]
ashley_list_data = ["Ashley", 25000]


hardik.display_details()

print(Employee.no_of_employees)

tanamay = Employee.from_list(tanmay_list_data)
ashley = Employee.from_list(ashley_list_data)

ashley.display_details()


print(Employee.is_holiday(datetime(2023, 2, 24)))