# test_assignment.py
import unittest
from santasolver.models import Employee
from santasolver.assignment import AssignmentEngine

class TestAssignmentEngine(unittest.TestCase):
    def test_assignments(self):
        employees = [Employee("Matthew King", "matthew.king@acme.com"), Employee("Benjamin Collins", "benjamin.collins@acme.com")]
        last_year = {"Isabella Scott": "isabella.scott@acme.com"}
        engine = AssignmentEngine(employees, last_year)
        assignments = engine.assign_secret_children()

        self.assertEqual(len(assignments), 2)
        for e, s in assignments.items():
            self.assertNotEqual(e.email, s.email)
            self.assertNotEqual(s.email, last_year.get(e.email))
