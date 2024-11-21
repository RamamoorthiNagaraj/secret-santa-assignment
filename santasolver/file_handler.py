# file_handler.py
import csv
from santasolver.models import Employee  

class FileHandler:
    @staticmethod
    def load_employees(file_path):
        employees = []
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employees.append(Employee(row["Employee_Name"], row["Employee_EmailID"]))
        except FileNotFoundError:
            print(f"Error: The file at {file_path} was not found.")
        except KeyError as e:
            print(f"Error: Missing expected column in the file - {e}.")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
        return employees

    @staticmethod
    def load_last_year_assignments(file_path):
        assignments = {}
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    assignments[row["Employee_EmailID"]] = row["Secret_Child_EmailID"]
        except FileNotFoundError:
            print(f"Error: The file at {file_path} was not found.")
        except KeyError as e:
            print(f"Error: Missing expected column in the file - {e}.")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
        return assignments

    @staticmethod
    def save_assignments(assignments, file_path):
        try:
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"])
                for employee, secret_child in assignments.items():
                    writer.writerow([employee.name, employee.email, secret_child.name, secret_child.email])
        except PermissionError:
            print(f"Error: Permission denied to write to {file_path}.")
        except Exception as e:
            print(f"Unexpected error occurred while saving assignments: {e}")
