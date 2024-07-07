people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

new_record = ('Oliver', 'Thomas', 32, 'Doctor', 'San Jose')
people_records.insert(0, new_record)

print("Modified list after adding new record:")
for person in people_records:
    print(person)

people_records[1], people_records[5] = people_records[5], people_records[1]

print("\nModified list after swapping elements with indexes 1 and 5:")
for person in people_records:
    print(person)

indexes_to_check = [6, 10, 13]
all_older_than_30 = all(people_records[idx][2] >= 30 for idx in indexes_to_check)

print("\nCondition check for people at indexes 6, 10, and 13 (age >= 30):")
print("All people have age >= 30:", all_older_than_30)
