# completa el código de la función
def amigos(a,b):
    num1=1
    num2=1
    suma1=0
    suma2=0
    while(num1<a):
        if(a%num1==0):
            suma1+=num1
        num1+=1
    while(num2<b):
        if(b%num2==0):
            suma2+=num2
        num2+=1
    if(suma1==b and suma2==a):
        return True
    else:
        return False
try:
    num1 = int (input("amigos: "))
    num2 = int (input("amigos: "))
    print(amigos(num1,num2))
except:
    print("Ingrese un numero")