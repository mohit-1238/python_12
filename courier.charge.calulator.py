# calculate courier charges based on package weight.

# Store the package weight in kilograms
weight = 5

# Check if the weight is less than or equal to 2 kg
if(weight <= 2):

    # Charge per kg for packages up to 2 kg
    charge = 50

    # Calculate total amount
    amount = weight * charge

    # Display weight, charge rate, and total amount
    print(f"weight is {weight}kg charge is Rs 50 per kg and amount is {amount}")

# Check if the weight is greater than 2 kg but less than or equal to 3 kg
elif(weight <= 3):

    # Charge per kg for packages up to 3 kg
    charge = 40

    # Calculate total amount
    amount = weight * charge

    # Display weight, charge rate, and total amount
    print(f"weight is {weight}kg charge is Rs 40 per kg and amount is {amount}")

# Execute when weight is greater than 3 kg
else:

    # Charge per kg for packages above 3 kg
    charge = 30

    # Calculate total amount
    amount = weight * charge

    # Display weight, charge rate, and total amount
    print(f"weight above {weight}kg charge is Rs 30 per kg and amount is {amount}")