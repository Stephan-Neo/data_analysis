import random

import numpy as np
import pandas as pd

# 1
x = np.arange(0, 1001, 1)
y = x**2 + 3*x + 5
z = [x_val / 2 if x_val % 2 == 0 else None for x_val in x]

married_sequence = ["yes", "undefined", "yes", "no", None]
married = [married_sequence[i % len(married_sequence)] for i in range(len(x))]

target_sequence = ["First", "Second", "Second", "Third", None]
target = [target_sequence[i % len(target_sequence)] for i in range(len(x))]

df_test = pd.DataFrame({'x': x, 'y': y, 'z': z, 'married': married, 'target': target})

# 2
print(df_test.head(4))
print(df_test.isnull().sum())
print(df_test.info())
print(df_test.describe())

# 3
mode_target = df_test['target'].mode()[0]
df_test['target'].fillna(mode_target, inplace=True)

mode_married = df_test['married'].mode()[0]
df_test['married'].fillna(mode_married, inplace=True)
print(df_test)

# 4
married_mapping = {'yes': 1, 'no': 0}
df_test['married'] = df_test['married'].map(married_mapping)
print(df_test)

# 5
numbers = [random.randint(0, 15) for _ in range(20)]
unique_numbers = [x for x in numbers if numbers.count(x) == 1]
print(unique_numbers)

def custom_sort(student):
    mark_order = {"Very good": 0, "Good": 1, "Bad": 2, "Very bad": 3}
    mark = student['mark']
    name = student['student_name']
    return (-mark_order[mark], name)

student_marks = [
    {'student_name': 'Alice', 'mark': 'Good'},
    {'student_name': 'Bob', 'mark': 'Very good'},
    {'student_name': 'Charlie', 'mark': 'Very bad'},
    {'student_name': 'David', 'mark': 'Bad'},
    {'student_name': 'Eve', 'mark': 'Good'},
    {'student_name': 'Frank', 'mark': 'Very good'},
    {'student_name': 'Grace', 'mark': 'Very bad'},
    {'student_name': 'Hannah', 'mark': 'Bad'},
    {'student_name': 'Ivy', 'mark': 'Good'},
    {'student_name': 'Jack', 'mark': 'Very good'},
    {'student_name': 'Karen', 'mark': 'Very bad'},
    {'student_name': 'Liam', 'mark': 'Bad'},
    {'student_name': 'Mia', 'mark': 'Good'},
    {'student_name': 'Nathan', 'mark': 'Very good'},
    {'student_name': 'Olivia', 'mark': 'Very bad'},
    {'student_name': 'Peter', 'mark': 'Bad'},
    {'student_name': 'Quinn', 'mark': 'Good'},
    {'student_name': 'Rachel', 'mark': 'Very good'},
    {'student_name': 'Sam', 'mark': 'Very bad'},
    {'student_name': 'Taylor', 'mark': 'Bad'},
]

sorted_student_marks = sorted(student_marks, key=custom_sort)

for student in sorted_student_marks:
    print(f"{student['student_name']}: {student['mark']}")
