#Descomponer un número
x=int(input())

if(x>=1000):
    print(x//1000,"M +",(x//100)%10,"C +",(x//10)%10,"D +",(x//1)%10,"U")
elif(x>=100):
    print((x//100)%10,"C +",(x//10)%10,"D +",(x//1)%10,"U")
elif(x>=10):
    print((x//10)%10,"D +",(x//1)%10,"U")
else:
    print((x//1)%10,"U")
    
  