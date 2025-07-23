tech_stack = {
     "Configuration":"Ansible",
     "Container":"CRIO",
     "Cloud Computing":"AWS",
     "Scripting":"Python",
     "Monitering":"Cloud Watch"
}



x = tech_stack["Monitering"]

print('before update dictionary',tech_stack )


# After update

tech_stack['Monitering'] = 'Grafana'

print('After updating tech_stack',tech_stack)

tech_stack['Testing'] = 'Unit Test'

print(tech_stack)



