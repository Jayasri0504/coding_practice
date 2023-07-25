n=int(input("enter a number to find factorial:")) #getting input from user
n=n+1                                             #to use range option in for loop
s=1                                               #initial assignment
for i in range(1,n):
    s=s*i                                         #to find factorial
print("the factorial of",n-1,"is",s)    
    
