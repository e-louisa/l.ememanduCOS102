print('''Welcome to the Week 1 Python Program.
Here we will calculate simple interest, compound interest and annuity plan.''')

#collecting the input
p_value = int(input('Enter the principal: '))
r_value = int(input('Enter the rate: '))
t_value = int(input('Enter the time: '))
n_value = int(input('Enter the value for N: '))
m_value = int(input('Enter the value for M: '))

#calculating the simple interest
amount_si = p_value * (1 + (r_value / 100) * t_value)

#calculating the compound interest
amount_ci = p_value * (1 + (r_value / n_value)) ** (n_value * t_value)

#calculating the annuity plan
amount_ap = ((p_value * m_value * t_value) * (1 + (r_value / n_value) ** (n_value * t_value)) - 1) * (r_value / n_value)

print("The value of simple interest is " + str(amount_si) + ".")
print("The value of compound interest is " + str(amount_ci) + ".")
print("The value of annuity plan is " + str(amount_ap) + ".")


