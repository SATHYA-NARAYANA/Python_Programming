# Problem statement: Find out how many months it take to reach the target revenue compared to current month revenue
current_revenue = 100000
target_revenue  = 200000
montly_growth_rate = 0.10
months = 0

while current_revenue < target_revenue:
    current_revenue = current_revenue + (current_revenue * montly_growth_rate)

    months = months + 1

    print (months , "month revenue is rs:", round(current_revenue))

print ("\n It will take", months, "months to reach the target revenue of Rs.",round(current_revenue))



# +=  
