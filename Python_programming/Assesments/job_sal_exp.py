print("Welcome to NSR Technologies!")

# List to store experience data
experience = []

# Input number of employees
num = int(input("Enter number of employees: "))

# Collect experience values from user
for i in range(num):
    exp = float(input(f"Enter experience for employee {i+1}: "))
    experience.append(exp)

    # Process the latest experience (simulate single employee processing)
    for exp_val in experience:
        if exp_val >= 10:
            category = "Senior employee"
            salary = 100000
        elif exp_val >= 5:
            category = "Mid-level employee"
            salary = 80000
        elif exp_val >= 2:
            category = "Junior-level employee"
            salary = 50000
        else:
            category = "Fresher"
            salary = 30000

        # Display result
        print("\nCongratulations!")
        print("Experience:", exp_val, "years")
        print("Your monthly salary is Rs.", format(salary, ","), "and you are a", category.lower() + ".")

    # Clear experience data after employee exits
    experience.clear()
