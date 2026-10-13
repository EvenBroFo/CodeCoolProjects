#def get_salary(person):
#   return person["salary"]


employees=[
    {"name": "alice", "salary": 50000},
    {"name": "bob", "salary": 60000},
    {"name": "charlie", "salary": 40000}
]

sorted_employees= sorted(employees, key=lambda person: person["salary"])

print(sorted_employees)