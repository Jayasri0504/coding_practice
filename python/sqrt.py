import math                                               #headerfile to do sqrt function
n=int(input("enter a number to check perfect square:"))   #getting input from user
x=math.sqrt(n)                                            #keyword to find sqrt
if(x==int(x)):                                            #to check if the result is whole number
    print("the entered number is a perfect sqr")
else:                                                     #if conition false then else block runs
    print("the entered is not a perfect sqr")
