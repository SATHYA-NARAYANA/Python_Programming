def admission():
    course = {
        "ETL Testing":35000,
        "Data Science": 45000,
        "Data Analytics": 40000,    
        "Data Engineering": 50000,
        "Machine Learning": 55000,
    }
    name = input("Enter your name: ").upper()
    course_name = input("Enter the course you want to enroll in: ").title()
    discount = input(f"Enter the discount percentage:{name} ")

    '''try:
        if course_name not in course:
            raise KeyError'''
    
admission()