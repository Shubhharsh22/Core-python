student_name=input("Enter the student Name:")
student_age=int(input("Enter the student age:"))

print("The name of student is {0} and age is {1} ".format(student_name,student_age))
#Example
if student_age >= 18:
    print("student is eligible for vote")
    if student_age >= 18 and student_age <= 25:
        print("student is eligible for vote and scholarship")
    elif student_age>25 and student_age<30:
        print("student is eligible for Job")
else:
    print("student is not eligible for vote,scholarship and job")
print(f"Bye Mr. {student_name} of age {student_age}")
for i in range(5,11,2):
    print(i)

for i in range(5,11):
    print(i)
        