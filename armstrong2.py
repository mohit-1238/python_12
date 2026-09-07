# 1-digit numbers: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 3-digit numbers: 153, 370, 371, 407
# 4-digit numbers: 1634, 8208, 9474



# Take a number to check whether it is an Armstrong number or not
num = int(input("Take a number to check whether it is an Armstrong number or not: "))

# Store original number because num will change during calculation
copy = num

# Variable to store sum of powered digits
sum = 0

# Variable to count total digits in the number
count = 0

# Count the number of digits
while(num > 0):
    count = count + 1
    num = num // 10

# Restore original number for further processing
num = copy

# Process each digit of the number
while(num > 0):

    # Get last digit
    ld = num % 10

    # Remove last digit from number
    num = num // 10

    # Power should be equal to total number of digits
    power = count

    # Used to calculate ld^count manually
    result = 1

    # Calculate digit raised to the power of count
    while(power > 0):
        result = result * ld
        power = power - 1

    # Add the powered digit to sum
    sum = result + sum

# Check whether original number equals calculated sum
if(copy == sum):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")