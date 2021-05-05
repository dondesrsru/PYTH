num = input('enter a number')
flag = False
if int(num) > 1:
    # check for factors
    for i in range(2, int(num)):
        if (int(num) % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
