# Calculate annual bonus based on employee salary

salary = 60000  # Employee's salary

# Check if salary is less than or equal to 20,000
if(salary <= 20000):

    bonus = (5 / 100) * salary  # Calculate 5% bonus
    amount = salary + bonus     # Add bonus to salary

    # Display salary, bonus, and total amount
    print(f"salary is {salary} bonus is {bonus} and amount is {amount}")

# Check if salary is between 20,001 and 50,000
elif(salary > 20000 and salary <= 50000):

    bonus = (10 / 100) * salary  # Calculate 10% bonus
    amount = salary + bonus      # Add bonus to salary

    # Display salary, bonus, and total amount
    print(f"salary is {salary} bonus is {bonus} and amount is {amount}")

# If salary is greater than 50,000
else:

    bonus = (15 / 100) * salary  # Calculate 15% bonus
    amount = salary + bonus      # Add bonus to salary

    # Display salary, bonus, and total amount
    print(f"salary is {salary} bonus is {bonus} and amount is {amount}")