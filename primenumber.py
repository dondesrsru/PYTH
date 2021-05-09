num = input('enter a number')
flag = False
if int(num) > 1:
    for i in range(2, int(num)):
        if (int(num) % i) == 0:
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
