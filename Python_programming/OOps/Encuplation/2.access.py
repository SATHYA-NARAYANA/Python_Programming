# how to access private memner in public
# we can access it indirectly defining privated variables inside a function

class emp():

    def __init__(self,eid,ename,sal):
        self.id = eid
        self.name = ename
        self.__sal = sal

    def display_sal(self):
        print("Emp id",self.id)
        print("Emp name",self.name)
        print("Emp sal",self.__sal)

obj_emp = emp(1005,'Rio',5000)
obj_emp.display_sal()
        
