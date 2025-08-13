# Dictionary in function

skills_dict = { "Language":"Python Language",
           "data Base":"Snowflake database",
           "ETL Tools":"Informatica ETL Tools"
        }
def nsr_skills_fun(skill):
    if skill in skills_dict:
        print(f"The trending {skill} is: {skills_dict[skill]}")
    else:
        print("The skill not found")

nsr_skills_fun(Language)

