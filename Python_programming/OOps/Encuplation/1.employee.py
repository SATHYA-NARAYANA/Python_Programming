class employee():
    def __init__(self,eid,ename,sal):

        self.emp_eid = eid
        self.emp_ename = ename
        self.__sal = sal

obj_employee = employee()

print("employee id is",obj_employee.emp_eid)
print("employee name is",obj_employee.emp_ename)
print("employee salary is",obj_employee.__sal)
