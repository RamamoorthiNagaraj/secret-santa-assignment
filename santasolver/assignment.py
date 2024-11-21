# assignment.py
import random

class AssignmentEngine:
    def __init__(self, employees, last_year_assignments):
        self.employees = employees
        self.last_year_assignments = last_year_assignments
        


    def assign_secret_children(self):
        if len(self.employees) < 2:
            raise ValueError("At least two employees are required for Secret Santa.")
        
        unassigned = self.employees[:]
        assignments = {}

        for employee in self.employees:
            possible_children = [
                e for e in unassigned
                if e.email != employee.email and e.email != self.last_year_assignments.get(employee.email)
            ]
            
            if not possible_children:
                raise ValueError("Constraints make it impossible to assign Secret Santa.")
            
            secret_child = random.choice(possible_children)
            assignments[employee] = secret_child
            unassigned.remove(secret_child)

        return assignments
