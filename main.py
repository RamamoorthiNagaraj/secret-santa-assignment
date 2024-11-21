# main.py
from santasolver.file_handler import FileHandler
from santasolver.assignment import AssignmentEngine
from santasolver.validator import Validator

def main():
    try:
        # File paths
        employee_file = "input/employees.csv"
        last_year_file = "input/last_year.csv"
        output_file = "output/assignments.csv"

        # Load data
        employees = FileHandler.load_employees(employee_file)
        last_year_assignments = FileHandler.load_last_year_assignments(last_year_file)

        # Validate input data
        Validator.validate_employees(employees)

        # Assign secret children
        engine = AssignmentEngine(employees, last_year_assignments)
        assignments = engine.assign_secret_children()

        # Save the new assignments
        FileHandler.save_assignments(assignments, output_file)

        print(f"Assignments completed successfully. Output saved to {output_file}.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
