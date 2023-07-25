x=int(input("enter a number to check prime or not:")) #getting a input to check prime or not
for i in range(2,x):    #using for loop for check a range of numbers from 2 to entered number
    if(x%i==0):         #if the entered no is divisible by any no.till the range it is not a prime
        print("the entered number is not a prime number")
        break


    #if the remainder is not zero it will break and go to next no. in that range
else:
    print("the entered number is a prime number")
        
