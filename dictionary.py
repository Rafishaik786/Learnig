num_students = int(input("Please enter number of students:"))
student_info = {}


def enter():
    print("you have entered %s students" % num_students)
    #student_info = {}
    student_data = ['mobile number : ', 'roll number : ', 'year : ', ]
    marks=['maths: ', 'physics: ', 'chemistry: ']
    for i in range(1,num_students+1):
        print('enter {} student details'.format(i))
        student_name = input("Name :")
        student_info[student_name] = {}
        for entry in student_data:
            student_info[student_name][entry] = int(input(entry)) #storing the marks entered as integers to perform arithmetic operations later on.
        print('enter your marks')
        for entry in marks:
            student_info[student_name][entry] = int(input(entry))


def show():
    print("Please enter student name ?")
    name = input("Student name : ")
    if name in student_info.keys():
        print ("Average student marks : ", str(sum(student_info[name].values())/3.0))
        print("details of %s  student:" % name, str((student_info[name].items())))
    else:
        print("please enter valid name")


enter()
show()
