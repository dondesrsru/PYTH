x=input('Enter an integer')
y=input('Enter another integer')
x=int(x)
y=int(y)  
for num in range(x,y + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  
if x>y:
    print('second number is lesser than first number. please rewrite the values in ascending order')
if x and y <=0:
    print('there are no prime numbers')
