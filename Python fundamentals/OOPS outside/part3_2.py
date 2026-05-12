import datetime

class Employee:

    @staticmethod
    def isWorkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

myDate = datetime.date(2024, 6, 22)
print(Employee.isWorkday(myDate))