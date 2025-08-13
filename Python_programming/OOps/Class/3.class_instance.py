class nsr_trining():
    n1 = "\nNSR technologies provides below training on data bases:"
    n2 = "\nNSR technologies provides below training on languages:"
    n3 = "\nNSR technologies provides below training on ETL Tools:"

    def database(self):
        db1 = "Oracle"
        db2 = "Snowflak"

        print(self.n1)
        print(db1)
        print(db2)

    def languages(self):
        l1 = "Python"
        l2 = "Java"

        print(self.n2)
        print(l1)
        print(l2)

    def etl_tools(self):
        e1 = "Informatica"
        e2 = "Talend"

        print(self.n3)
        print(e1)
        print(e2)

instance_variable_class = nsr_trining()


instance_variable_class.database()
instance_variable_class.languages()
instance_variable_class.etl_tools()


# Function defined outside class

# method if function define inside class

