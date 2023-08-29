#Descomponer un número
import random
dig1=random.randrange(10)
dig2=random.randrange(10)
dig3=random.randrange(10)
dig4=random.randrange(10)
print(dig1,dig2,dig3,dig4)
numb=int(input("ingrese un numero de 4 digitos: "))
u1=numb//1000
u2=(numb-u1*1000)//100
u3=(numb-(u1*1000+u2*100))//10
u4=numb-(u1*1000+u2*100+u3*10)
print(u1,"M +",u2,"C +",u3"D +",u4,"U")      