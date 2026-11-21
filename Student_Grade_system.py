students = {
"Ali": 85,
"Sara": 72,
"Ahmed": 35,
"Ayesha": 91,
"Usman": 55
           }

def calculate_grade(marks):

    if marks >= 80:
        return "A"

    elif marks >= 60 and marks <= 79:
        return "B"

    elif marks >= 40 and marks <= 59:
        return "C"

    else:
        return "Fail"



cout_pass = 0
count_fail = 0

for name , marks in students.items():
    grade = calculate_grade(marks)
    if grade == "Fail":
        count_fail += 1
    else:
        cout_pass += 1
    print(f"Name:{name} Marks:{marks} Grade:{grade}")


print(f"pass_students:{cout_pass} , fail_students:{count_fail}")
