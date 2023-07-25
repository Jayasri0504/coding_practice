a=int(input("enter any number to check armstrong:"))              #getting input from the user
digits=int(input("pls enter the no. of digits in your number:"))  #to assign the value of power
b=a                                                               #to check if condition
s=0                                                               #initial assignment
while(a!=0):                                                      #this loop runs untill the "a" value gets zero
   remainder=a%10                                                 #divinding by 10 to get separate digits
   s=s+remainder**digits
   a=a//10
print("the result is:",s)
if(s==b):                                                         #if block to check the entered no.is equal to the resultant number
    print("the entered number is armstrong number")
else:
    print("the entered number is not a armstrong number")
