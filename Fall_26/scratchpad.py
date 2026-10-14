# Replace the placeholder values with your actual details

teacher_name: str = input("Your Name and School District")

courses_taught: list[str] = input("List of Courses (comma separated)").split(",")

pathway: str = input("Your Pathway if applicable")

cs_misconception: str = input(f"One {4 > 5} CS Misconception you had")

print("Teacher Name:", teacher_name)
print("Courses Taught:", courses_taught)
print("Pathway:", pathway)
print("CS Misconception:", cs_misconception)

