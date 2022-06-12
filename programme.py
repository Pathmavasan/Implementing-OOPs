from inspect import _void
from course import Course
from student import Student
class Programme:
    courses_count=0
    the_courses=[]
    Students=[]
    def __init__(self,name):
        self.ProgrammeName=name
    def __str__(self):
        return "Total Course Count"+self.courses_count
    def addCourse(self,coursename):
        NewAddedCourse = Course(coursename,self.courses_count)
        self.the_courses.append(NewAddedCourse)
        self.courses_count+=1
    def addNewCourse(self,coursename):
        NewAddedCourse = Course(coursename,self.courses_count)
        self.the_courses.append(NewAddedCourse)
        self.courses_count+=1
        return NewAddedCourse
    def displayCourses(self):
        for i in self.the_courses:
            print(i.id,i.CourseName)
    def removeCourse(self,courseid):
        ToBeDeleted=self.getCourseById(courseid)
        self.the_courses.remove(ToBeDeleted)
        del ToBeDeleted
        print("Course Deleted Succesfully")
    def getCourseById(self,courseid):
        for i in self.the_courses:
            if i.id==courseid: return i
    def addStudent(self,StudentName,courseid):
        CourseToAdd = self.getCourseById(courseid)
        student = Student(CourseToAdd,StudentName,Student.s_id)
        CourseToAdd.Students.append(student)
        self.Students.append(student)
        Student.s_id+=1
        print("Student Added Successfully")
        print("StudentName:",student.name)
        print("Studentid:",student.id)
        print("Student Added Successfully in",CourseToAdd.CourseName)
        return student
    def printStudent(self):
        for i in self.Students:
            print(i.id,i.name)
    def removeStudent(self,studentid):
        StudentToDelete = self.getStudentById(studentid)
        self.Students.remove(StudentToDelete)
        for i in self.the_courses:
            i.removeStudent(StudentToDelete)
        del StudentToDelete
    def getStudentById(self,studentid):
        for i in self.Students:
            if i.id==studentid: 
                return i
    def printAllStudentDetails(self):
        for i in self.Students:
            print(i.id, i.name)
            print("Enrolled Courses")
            for j in i.Courses:
                print(" ",j.CourseName)
    def AddStudentToACourse(self,course_id,student_id):
        course=self.getCourseById(course_id)
        student=self.getStudentById(student_id)
        if course not in student.Courses:
            student.Courses.append(course)
            course.Students.append(student)
            student.CoursesNotGraded.append(course)
            print("Student Added Successfully in",course.CourseName)
        else:
            print("Student is Already In The Course")
        return student
    def getStudentForCourse(self,course_id):
        course=self.getCourseById(course_id)
        for i in course.Students:
            print(i.name)
    def enterGradeForAStudent(self,student_id):
        student = self.getStudentById(student_id)
        student.gradeStudent()
        student.CoursesNotGraded=[]
        return student
    def AddStudentInAllCourse(self,StudentName):
        #CourseToAdd,StudentName,Student.s_id
        student = self.addStudent(StudentName,self.the_courses[0].id)       
        for i in self.the_courses[1:]:
            self.AddStudentToACourse(i.id,student.id)
        return student
    def printresultByStudentId(self,student_id):
        student= self.getStudentById(student_id)
        student.printGrades()
    def printParticularStudentDetails(self,Student_id):
        student = self.getStudentById(Student_id)
        print("Student Details...\n\n")
        print(student.name)
        print("The Courses He Enrolled")
        for i in student.Courses:
             print(" ",i.CourseName)
        for i in student.Courses:
            counter=1
            try:
                for j in student.Allgrades[i]:
                    print("  Assignment",counter,"grade for the course",i.CourseName,"is",j)
                    counter+=1
            except:
                print(" The Student Haven't Graded Yet! :-("); break
    def printStudentDetailsNotGraded(self,StudentsNotGradedList):
        for i in StudentsNotGradedList:
            StudentDetail = self.getStudentById(i)
            print(StudentDetail.id,StudentDetail.name)