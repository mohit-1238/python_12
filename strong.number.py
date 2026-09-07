# find & print strong number

num = 145                    # original number

strong = num % 10            # get last digit (5)
num = num // 10              # remove last digit, num becomes 14

strong = 5                   # store digit 5
count = 1                    # counter for factorial
result_1 = 1                 # factorial result of 5

while(count <= strong):      # calculate 5!
    result_1 = count * result_1
    count = count + 1

strong = num % 10            # get next digit (4)
num = num // 10             # remove digit 4, num becomes 1

strong = 4                   # store digit 4
count = 1                    # reset counter
result_2 = 1                 # factorial result of 4

while(count <= strong):      # calculate 4!
    result_2 = count * result_2
    count = count + 1

strong = num % 10            # get next digit (1)

strong = 1                   # store digit 1
count = 1                    # reset counter
result_3 = 1                 # factorial result of 1

while(count <= strong):      # calculate 1!
    result_3 = count * result_3
    count = count + 1

    sum = result_1 + result_2 + result_3   # add all factorials
    print(sum)                             # print result (145)    