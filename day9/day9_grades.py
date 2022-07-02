def student_evaluation(database):
    for person in database:
        score = student_grades[person]
        if score < 70:
            print(f"{person}: Fail")
        elif score < 81:
            print(f"{person}: Acceptable")
        elif score < 91:
            print(f"{person}: Exceeded expectations")
        else:
            print(f"{person}: Outstanding")


student_grades = {}

student = input("Insert the name of the student\n")

while student != '0':
    student_grades[student] = int(input("Insert the score\n"))
    student = input("Insert the name of the student\n")

student_evaluation(student_grades)
