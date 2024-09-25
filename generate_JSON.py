import json
import random

# Generate 100 employee records
employees = []
for i in range(1, 101):
    employee = {
        "employee_id": i,
        "first_name": f"FirstName{i}",
        "last_name": f"LastName{i}",
        "age": random.randint(22, 60),
        "department": {
            "dept_id": random.randint(101, 120),
            "dept_name": f"Dept{random.randint(1, 20)}"
        },
        "address": {
            "street": f"{random.randint(1000, 9999)} Some St",
            "city": random.choice(["San Francisco", "New York", "Chicago", "Los Angeles", "Seattle"]),
            "state": random.choice(["CA", "NY", "IL", "WA", "TX"]),
            "zip": f"{random.randint(10000, 99999)}"
        },
        "skills": random.sample(["Python", "Spark", "AWS", "Scala", "Kafka", "SEO", "Google Analytics"], 3)
    }
    employees.append(employee)

with open("employees.json", "w") as f:
    json.dump(employees, f, indent=2)

# Generate 100 department budget records
departments = []
for i in range(101, 201):
    department = {
        "dept_id": i,
        "budget": random.randint(200000, 800000),
        "manager": f"Manager{i}"
    }
    departments.append(department)

with open("department_budget.json", "w") as f:
    json.dump(departments, f, indent=2)