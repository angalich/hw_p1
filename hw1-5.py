revenue = int(input("Enter revenue: "))
costs = int(input("Enter costs: "))
profit = revenue - costs
print("Company profit:", profit)
if profit > 0:
    profitability = profit/revenue
    employee = int(input("Enter number of employers: "))
    profit_per_e = profit/employee
    print("Company profitability: ", profitability)
    print("Profit per employee: ", profit_per_e)
else:
    print("Bad company profit")
#+