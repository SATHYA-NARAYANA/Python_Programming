tech_stack = {
     "Configuration":"Ansible",
     "Container":"CRIO",
     "Cloud Computing":"AWS",
     "Scripting":"Python", 
     "Monitering":"Cloud Watch"
}
for tech, course in tech_stack.items():
    print(f'Your loved {tech}: course matches with {course}')
'''
print("Do you like to suggest / recommend some more tech stack")
#new_course_suggestion = []

new_course_suggestion = {}


while True:
    new_tech_stack = input("Enter Tech stack name:")
    if new_tech_stack == 'Done':
        break

    if new_tech_stack not in tech_stack:
        #new_course_suggestion.append(new_tech_stack)
        new_course_suggestion.update(new_tech_stack)
        print(f"{new_tech_stack} reccomeded succesfully.")
        
        print(tech_stack)



        print("Do you like to suggest / recommend some more tech stack \n")
#new_course_suggestion = {}

'''
