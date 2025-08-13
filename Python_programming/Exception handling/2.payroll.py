class nsr_payroll():
    print("\t\tWelcome to NSR Employee payroll calculate\n")

    def cal_sal(self):
        try:
            hourly_rate =float(input("Enter hourly rates for employees \t(Rs):"))
            hours_worked = float(input("Enter number of hours worked:\t"))

            if hourly_rate > 0 and hours_worked >0:
                totalsal = hourly_rate * hours_worked
                print(f"\n Employee monthly sal : Rs.{totalsal:.2f}")
            else:
                print("\n Hourly rate and Hours worked must be positive value")
        except ValueError:
            print("\n Error: Please enter valid numeric value for hourly rate and hoursworked")


payroll = nsr_payroll()
payroll.cal_sal()         
