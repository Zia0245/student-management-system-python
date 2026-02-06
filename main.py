
students = []

def show_menu():
    print("\n==============================")
    print("   Student Management System")
    print("==============================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("==============================")

def add_student():
    print("\n--- Add New Student ---")
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    age = input("Enter age: ")
    grade = input("Enter grade/class: ")

    student = {
        "name": name,
        "roll_no": roll_no,
        "age": age,
        "grade": grade
    }

    students.append(student)
    print("\nStudent added successfully!")

def view_students():
    if not students:
        print("\nNo students found!")
        return

    print("\n--- All Students ---")
    print(f"{'Name':15} {'Roll No':10} {'Age':5} {'Grade':10}")
    print("-" * 45)

    for s in students:
        print(f"{s['name']:15} {s['roll_no']:10} {s['age']:5} {s['grade']:10}")

def search_student():
    roll_no = input("\nEnter roll number to search: ")

    for s in students:
        if s['roll_no'] == roll_no:
            print("\n--- Student Found ---")
            print("Name :", s['name'])
            print("Roll :", s['roll_no'])
            print("Age  :", s['age'])
            print("Grade:", s['grade'])
            return

    print("\nStudent not found!")

def update_student():
    roll_no = input("\nEnter roll number to update: ")

    for s in students:
        if s['roll_no'] == roll_no:
            print("\n--- Update Student ---")
            print("Press Enter to keep current value")

            name = input(f"New name ({s['name']}): ")
            age = input(f"New age ({s['age']}): ")
            grade = input(f"New grade ({s['grade']}): ")

            if name:
                s['name'] = name
            if age:
                s['age'] = age
            if grade:
                s['grade'] = grade

            print("\nStudent updated successfully!")
            return

    print("\nStudent not found!")

def delete_student():
    roll_no = input("\nEnter roll number to delete: ")

    for i, s in enumerate(students):
        if s['roll_no'] == roll_no:
            confirm = input(f"Delete {s['name']}? (y/n): ")
            if confirm.lower() == 'y':
                students.pop(i)
                print("\nStudent deleted successfully!")
            else:
                print("\nDeletion cancelled!")
            return

    print("\nStudent not found!")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice!")

main()
