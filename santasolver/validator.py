# validator.py
class Validator:
    @staticmethod
    def validate_employees(employees):
        if not employees:
            raise ValueError("Employee list is empty.")
        emails = [e.email for e in employees]
        if len(emails) != len(set(emails)):
            raise ValueError("Duplicate email IDs found in employee list.")
