class nsr_bangalore():
    bng_branch = '\nNSR technologies bangalore branch provides following courses:'

    def courses(self):
        course = {"testing":"ETL Testing","Database":"Snowflake","Language":"Python"}
        print(self.bng_branch)

        for a in course:
            print(course[a])

class nsr_hyd():
    hyd_branch = '\nNSR technologies hydrabad branch provides following courses:'

    def courses(self):
        course = {"Automation":"Python","Tools":"Informatica","Cloud":"AWS S3"}
        print(self.hyd_branch)

        for b in course:
            print(course[b])


class nsr_chennai():
    chh_branch = '\nNSR Technologies Chennai branch provides following courses:'

    def courses(self):
        course = {"Mobile":"Mobile testing","API Testing":"Postman","Bigdata":"Hadoop"}
        print(self.chh_branch)

        for c in course:
            print(course[c])

bangalore_branch = nsr_bangalore()
hyderbad_branch = nsr_hyd()
chennai_branch = nsr_chennai()

for i in (bangalore_branch,hyderbad_branch,chennai_branch):
    i.courses()

#bangalore_branch.courses()





            
