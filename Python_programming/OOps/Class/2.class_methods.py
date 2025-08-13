class cls_students():

    sid = 1001
    sname = 'Sam'
    branch = 'IT'

    def stu_details(self):
        stu_no = 1
        name = "Kumar"

        print("\n student details : method: student id :",stu_no)
        print("stu_details method: student name:",name)

        print("\n parent property:",self.sname)


    def nsr_course(self):
        nsr = "Hello NSR"
        course = "Python"

        print("\n NSR method:",nsr)
        print("\n  course methos",course)

        print("\n parent property:", self.sname)
        print("\n parent branch", self.branch)


# instance variable "obj_student_cls"
obj_student_cls = cls_students()

obj_student_cls.stu_details()
obj_student_cls.nsr_course()
