class nsr_bangalore():
    bng_branch = '\nNSR technologies bangalore branch provides following courses:'

    def courses(self):
        course = {"testing":"ETL Testing","Database":"Snowflake","Language":"Python"}
        print(self.bng_branch)

        for a in course:
            print(course[a])

class nsr_hyd(nsr_bangalore):
    hyd_branch = '\nNSR technologies hydrabad branch provides following courses:'

    def courses(self):
        course = {"Automation":"Python","Tools":"Informatica","Cloud":"AWS S3"}
        print(self.hyd_branch)

        for b in course:
            print(course[b])


  

#bangalore_branch = nsr_bangalore()
hyderbad_branch = nsr_hyd()
hyderbad_branch.courses()
 
#bangalore_branch.courses()





            
