# Different Python Data Types
name = "Siva Mani Krishna"
age = 19
cgpa = 9.01
is_placed = True
print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_placed))

#Numeric Data Types
integer_num = 100
float_num = 99.99
complex_num = 4 + 5j

print(integer_num)
print(float_num)
print(complex_num)

#Sequence Data Types
language = "Python"

subjects = ["Python", "AI", "Machine Learning"]

marks = (90, 95, 98)

print(language)
print(subjects)
print(marks)

#Mutable vs Immutable
# Mutable Example

skills = ["Python", "AI"]

skills.append("FastAPI")

print(skills)

#Type Conversion
age = "22"

print(type(age))

age = int(age)

print(type(age))
