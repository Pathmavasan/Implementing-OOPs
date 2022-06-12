class Course:
    def __init__(self,CourseName,idForCourse):
        self.id=idForCourse
        self.CourseName=CourseName
        self.Students=[]
    def __str__(self):
        return self.CourseName
    def removeStudent(self,StudentObject):
        try:  self.Students.remove(StudentObject)
        except: pass