# Electricity Bill Generator Program

# Take input from user for total electricity units consumed
unit = float(input("Enter your units: "))

# Initialize bill amount with 0
bill = 0

# If units are less than or equal to 100
if(unit <= 100):

    # Charge Rs 1.5 per unit for all units
    bill = unit * 1.5

# If units are greater than 100 and less than or equal to 200
elif(unit <= 200):

    # First 100 units
    fp = 100

    # Remaining units after first 100
    sp = unit - 100

    # Calculate bill:
    # First 100 units at Rs 1.5/unit
    # Remaining units at Rs 2.5/unit
    bill = fp * 1.5 + sp * 2.5

# If units are greater than 200
else:

    # First 100 units
    fp = 100

    # Second 100 units
    sp = 100

    # Remaining units beyond 200
    tp = unit - 200

    # Calculate bill:
    # First 100 units at Rs 1.5/unit
    # Next 100 units at Rs 2.5/unit
    # Remaining units at Rs 3.5/unit
    bill = fp * 1.5 + sp * 2.5 + tp * 3.5

# Display final bill amount
print(f"Bill for #{unit} units is Rs {bill}/-")