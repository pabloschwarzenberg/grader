#Descomponer un número
numero=(input("ingrese un numero de maximo 4 digitos:"))
a=len(numero)
numero=eval(numero)
if(a==4):
    m=numero//1000
    c=(numero%1000)//100
    d=((numero%1000)%100)//10
    u=(((numero%1000)%100)%10)//1
    print(m,"M +", c,"C +", d,"D +", u,"U")
elif(a==3):
    m=numero//100
    c=(numero%100)//10
    d=((numero%100)%10)//1

    print(m,"C +", c,"D +", d,"U")
elif(a==2):
    m=numero//10
    c=(numero%10)//1

    print(m,"D +", c,"U")
elif(a==1):
    m=numero

    print(m,"U")