class Student:
    s_id=0
    def __init__(self,courseObject,Name,idForStu):
        self.name=Name
        self.id=idForStu
        self.Courses=[]
        self.Courses.append(courseObject)
        self.Allgrades=dict()
        self.CoursesNotGraded=[]
        self.CoursesNotGraded.append(courseObject)
    def gradeStudent(self):
        #if self.Allgrades==dict():
        if len(self.CoursesNotGraded)>=4 or (len(self.CoursesNotGraded)+len(self.Allgrades))>=4:
            for i in self.CoursesNotGraded:
                print("Enter the Grades for the Course:",i.CourseName)
                Grades=[]
                for j in range(5):
                    print("Enter the grade of Assignment",j+1,"As P/F P--Pass F--Fail")
                    while 1:
                        try:
                            Grade=input()
                        except: print("Enter a Valid Grade,P/F..")
                        else:
                            Grade=Grade.upper()
                            if Grade!='P' and Grade!='F': print("Enter a Valid Grade,P/F.."); continue
                            else: break
                    if Grade=='P': Grades.append("Pass")
                    else: Grades.append("Fail")
                self.Allgrades[i]=Grades
                print("The Grades For The Course:",i.CourseName,"are\n",self.Allgrades[i])
            print("Graded The Student Successfully!")
        else:
            print("The Student is only enrolled in 3 or less number of courses")
    def printGrades(self):
        if len(self.CoursesNotGraded)==0:
            try:
                L=self.isPass()
            except:
                print("Some Students Haven't Graded yet!!")
            else:
                if L==False:
                    print("The Studen't Haven't Graded in All Courses yet!!")
                else:
                    if L[0]:
                        print("Student",self.name,end=' ')
                        if(L[1]>=17 and L[2]==True):
                            print("Passed In Distinction with",L[1],"Assignments Passed")
                        else:
                            print("Passed")
                    else:
                        print("Student",self.name,"is failed")
        else:
            print("Some Students Haven't Graded yet!!")
    def isPass(self):
        TotalAssignmentPassCount,IsFivePassed=0,False
        for i in self.Courses:
            CourseAssignmentPassCount=self.Allgrades[i].count("Pass")
            if CourseAssignmentPassCount<3: return [False,0,0]
            TotalAssignmentPassCount+=CourseAssignmentPassCount
            if CourseAssignmentPassCount==5: IsFivePassed=True
        return [True,TotalAssignmentPassCount,IsFivePassed]