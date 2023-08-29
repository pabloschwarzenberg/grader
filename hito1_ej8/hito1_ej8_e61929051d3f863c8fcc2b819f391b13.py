#Descomponer un número
Numero=int(input("Ingrese un Numero de hasta 4 digitos: "))
u1=Numero//1000

u2=(Numero-u1*1000)//100

u3=(Numero-(u1*1000+u2*100))//10

u4=Numero-(u1*1000+u2*100+u3*10)

print(u1,"M","+",u2,"C","+",u3,"D","+",u4,"U")      