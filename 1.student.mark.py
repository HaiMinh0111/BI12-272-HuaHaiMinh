students = []
courses = []

def add_student(students, id, name, dob):
    for student in students:
        if student['id'] == id:
            print(f"A student with ID {id} already exists")#Kiểm tra student ID có bị trùng với ID có sẵn hay ko
            return
    
    student = {"id": id, "name": name, "dob": dob}
    students.append(student)
    print(f"Added student: {student}")

def add_student_from_user(students):
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")
    add_student(students, id, name, dob)

def add_course(courses, id, name):
    for course in courses:
        if course['id'] == id:
            print(f"A course with ID {id} already exists")#Kiểm tra course ID có bị trùng với ID có sẵn
            return
    
    course = {"id": id, "name": name}
    courses.append(course)
    print(f"Added course: {course}")

def add_course_from_user(courses):
    id = input("Enter course ID: ")
    name = input("Enter course name: ")
    add_course(courses, id, name)

def add_mark_from_user(courses, students):
    course_id = input("Enter course ID: ")
    student_id = input("Enter student ID: ")
    mark = input("Enter mark: ")

    course = None
    for c in courses:
        if c['id'] == course_id:
            course = c
            break
    else:
        print(f"No course with ID {course_id} found")
        return

    for student in students:
        if student['id'] == student_id:
            if 'marks' not in student:
                student['marks'] = {}
            student['marks'][course_id] = mark
            break
    else:
        print(f"No student with ID {student_id} found")

    print(f"Added mark for student {student_id} in course {course_id}: {mark}")

def main():
    add_student(students, "BI12-272", "Hứa Hải Minh", "01/11/2003")
    add_student(students, "BI12-307", "Phạm Hải Nam", "29/04/1999")
    add_student(students, "BI12-396", "Phùng Đức Thái", "31/10/2003")

    add_course(courses, "APWP", "Advanced Programming with Python")
    add_course(courses, "SE", "Software Engineering")
    add_course(courses, "OOP", "Object-Oriented Programming")

    add_mark_from_user(courses, students)

    print("Add student:")
    add_student_from_user(students)

    print("Add course:")
    add_course_from_user(courses)

    print("Add mark:")
    add_mark_from_user(courses, students)

    print(courses)
    print(students)

if __name__ == '__main__':
    main()
