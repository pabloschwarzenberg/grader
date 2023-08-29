#Cálculo del dígito verificador de un rut
 #a continuacion identificaremos el digito verificador 
numero = int(input("Ingrese el rut : "))
#separamos el rut por cada digito 

diesmilmil = (numero%100000000)//10000000

milmil = (numero%10000000)//1000000

cienmil = (numero%1000000)//100000

diesmil = (numero%100000)//10000 

mil = (numero%10000)//1000

centena = (numero%1000)//100

decena = ((numero%1000)%100)//10

unidad = ((numero%1000)%100)%10
#print(diesmilmil,"diesmilmil +",milmil,"milmil +",cienmil,"cienmil +",diesmil,"diesmil +",mil,"M +",centena,"C +",decena,"D +",unidad,"U")
#a cada digito de el rut se multiplica por 2,3,4,5,6,7 y se repite 
A=unidad*2
B=decena*3
C=centena*4
D=mil*5
E=diesmil*6
F=cienmil*7
G=milmil*2
H=diesmilmil*3

#aplicamos las siguientes ecuaciones 
suma=A+B+C+D+E+F+G+H
#print(suma,"suma")
division=suma//11
#print(division)

#tengo que sacar el resto de la division

resto=round(division,1)
#print(division,"divi",resto,"resto")
total=suma-(11*division)
resultado=11-total

#si el resultado es igual a 11 es 0 y si es igual a 10 es K
if resultado== 11:
    print("dv=",0)

elif resultado== 10:
    print("dv=K")

print("dv=",resultado)