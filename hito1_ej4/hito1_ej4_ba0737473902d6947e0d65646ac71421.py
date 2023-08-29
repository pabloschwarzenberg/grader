number= int(input("enter a number: "))
b=""
while (number)>0:
    x=(number - 2*((number)//2))
    number= number//2
    b = str(x)+b

print ("resultado=",b)