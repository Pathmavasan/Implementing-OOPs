from programme import Programme
#Creating a Programme..
data_science_programme=Programme("Data Science Programme")

#Adding Courses to the Programme

data_science_programme.addCourse("Python Programming Course")
data_science_programme.addCourse("Data Mining And Machine Learning Course")
data_science_programme.addCourse("Python Programming Course")
data_science_programme.addCourse("Text analytics course")

#Declaring the Variables

CoursesId=[i.id for i in data_science_programme.the_courses]
StudentsId=[]
StudentsNotGraded=[]
#Running The Portal
while 1:
    #Welcoming
    print("Welcome To The Portal")
    #Asking Input from The User
    print("1.Access The Courses\n2.Add a Course\n3.Remove a Course\n4.Access the Students\n5.Exit")
    try:
        choice=int(input())
    except: print("Enter a Valid Number...\n"); continue
    else:
        if(choice>6 or choice<0): print("Enter a Valid Number..\n"); continue #Redirecting Again
        elif choice==1:
            #Displaying The Choices
            print("1.Add New Students\n2.Remove Students\n3.Grade a Student\n4.See The Student Details\n5.Add Existing Students to a Course\n6.Display Students in Specific Course\n7.Add A New Student In All Courses\n8.RESULTS!!\n9.Back")
            while 1:
                try:
                    Choice_for_course=int(input())
                except: print("Enter a Valid Number..")
                else: 
                    if(0<Choice_for_course<10): break
                    else: print("Enter a Valid Number.."); continue
            #Adding a Student
            if Choice_for_course==1:
                print("Enter the Student Name To Be Added..")
                StudentName=input()
                print("Enter the Course Number to join..\n")
                data_science_programme.displayCourses()
                while True:
                    try:
                        CourseToBeAdded=int(input())
                    except: print("Enter a Valid Course Number..")
                    else:
                        if(CourseToBeAdded in CoursesId): break
                        else: print("Enter a Valid Course Number.."); continue
                StudentAdded=data_science_programme.addStudent(StudentName,CourseToBeAdded)
                StudentsId.append(StudentAdded.id)
                StudentsNotGraded.append(StudentAdded.id)
                StudentsNotGraded=sorted(set(StudentsNotGraded))
            #Deleting a Student
            elif Choice_for_course==2:
                print("Which Students Data You Need To Delete?..")
                data_science_programme.printStudent()
                print("Enter -1 to Exit")
                while 1:
                    try:
                        Student_id=int(input())
                    except: print("Enter a Valid Student id Number..")
                    else: 
                        if(Student_id in StudentsId or Student_id==-1): break
                        else: print("Enter a Valid Student id Number.."); continue
                if(Student_id==-1): continue
                else:
                    StudentsId.remove(Student_id)
                    data_science_programme.removeStudent(Student_id)
                    StudentsNotGraded.remove(Student_id)
            elif Choice_for_course==3:
                if StudentsNotGraded!=[]:
                    print("You're Gonna grade a Student in all Of His Courses")
                    print("Enter the Student Id")
                    data_science_programme.printStudentDetailsNotGraded(StudentsNotGraded)
                    print("Enter -1 to Exit")
                    while 1:
                        try:
                            Student_id=int(input())
                        except: print("Enter a Valid Student id Number..")
                        else: 
                            if(Student_id in StudentsId or Student_id==-1): break
                            else: print("Enter a Valid Student id Number.."); continue
                    if(Student_id==-1): continue
                    else:
                        StudentDetails=data_science_programme.enterGradeForAStudent(Student_id)
                        StudentsNotGraded.remove(StudentDetails.id)
                else:
                    print("All Students Have Been Graded in All Courses")
            elif Choice_for_course==4: data_science_programme.printAllStudentDetails()
            elif Choice_for_course==5:
                print("Enter the Course id where the Student to be Added")
                data_science_programme.displayCourses()
                print("Enter -1 to Exit")
                while 1:
                    try:
                        course_id=int(input())
                    except: print("Enter a Valid Course Number..")
                    else: 
                        if(course_id in CoursesId or course_id==-1): break
                        else: print("Enter a Valid Course Number.."); continue
                if(course_id==-1): continue
                else:
                    print("Enter the Student id to Add in Course",course_id)
                    data_science_programme.printAllStudentDetails()
                    while 1:
                        try: Student_id=int(input())
                        except: print("Enter a Valid Student Detail")
                        else:
                            if(Student_id in StudentsId): break
                            else: print("Enter a Valid Student Detail"); continue
                    StudentDetails=data_science_programme.AddStudentToACourse(course_id,Student_id)
                    StudentsNotGraded.append(StudentDetails.id)
                    StudentsNotGraded=sorted(set(StudentsNotGraded))
            elif Choice_for_course==6:
                print("Enter the Course id")
                data_science_programme.displayCourses()
                print("Enter -1 to Exit")
                while 1:
                    try:
                        course_id=int(input())
                    except: print("Enter a Valid Course Number..")
                    else: 
                        if(course_id in CoursesId or course_id==-1): break
                        else: print("Enter a Valid Course Number.."); continue
                if(course_id==-1): continue
                else:
                    data_science_programme.getStudentForCourse(course_id)
            elif Choice_for_course==7:
                print("Enter the Student Name To Be Added..")
                StudentName=input()
                StudentDetails=data_science_programme.AddStudentInAllCourse(StudentName)
                StudentsId.append(StudentDetails.id)
                StudentsNotGraded.append(StudentDetails.id)
                StudentsNotGraded=sorted(set(StudentsNotGraded))
            elif Choice_for_course==8:
                for i in StudentsId:
                    data_science_programme.printresultByStudentId(i)
            elif Choice_for_course==9: continue
        elif choice==2:
            #Adding a New Course
            print("Enter a Course Name")
            X=data_science_programme.addNewCourse(input())
            CoursesId.append(X.id)
        elif choice==3:
            #Deleting an Existing Course
            print("Which Course do you need to delete")
            data_science_programme.displayCourses()
            print("Enter -1 to Exit")
            while 1:
                try:
                    course_id=int(input())
                except: print("Enter a Valid Course Number..")
                else: 
                    if(course_id in CoursesId or course_id==-1): break
                    else: print("Enter a Valid Course Number.."); continue
            if(course_id==-1): continue
            else:
                CoursesId.remove(course_id)
                data_science_programme.removeCourse(course_id)
        elif choice==4:
            print("You're gonna access the Students..\n")
            print("Enter the Student Id To Access")
            data_science_programme.printStudent()
            print("Enter -1 to Exit")
            while 1:
                try:
                    Student_id=int(input())
                except: print("Enter a Valid Student id Number..")
                else: 
                    if(Student_id in StudentsId or Student_id==-1): break
                    else: print("Enter a Valid Student id Number.."); continue
            if(Student_id==-1): continue
            else:
                data_science_programme.printParticularStudentDetails(Student_id)
        elif choice==5: print("Thank You"); break