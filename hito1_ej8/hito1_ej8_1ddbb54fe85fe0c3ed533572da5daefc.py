#Descomponer un número
num=input("Ingrese un número")

if int(num)>=1000 and int(num)<=9999:
    
    a=int(num[0:1])
    b=int(num[1:2])
    c=int(num[2:3])
    d=int(num[3:4])

    print(a,"M","+",b,"C","+",c,"D","+",d,"U")
elif int(num)>=100 and int(num)<=999:
    
    a=int(num[0:1])
    b=int(num[1:2])
    c=int(num[2:3])
  

    print(a,"C","+",b,"D","+",c,"U")

elif int(num)>=10 and int(num)<=99:
    
    a=int(num[0:1])
    b=int(num[1:2])
    
  

    print(a,"D","+",b,"U")

elif int(num)>=0 and int(num)<=9:
    
    a=int(num[0:1])
  
  

    print(a,"U")

else:
    print("Error")