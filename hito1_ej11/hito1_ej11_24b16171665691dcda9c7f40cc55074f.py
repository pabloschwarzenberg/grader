#Cajero Automático
dinero_total = 1000000
valor_ingresado =[10334151,1803,100000]

valor_1 =int(input("Ingrese usuario:"))
valor_2 =int(input("Ingrese clave:"))

persona = [valor_1,valor_2]
contador =1

lista=[0,0]

dinero20 = 20
dinero10 = 40
dinero5 = 40
while persona[1]!= persona[1] and contador <3:
    print("La clave ingresada es incorrecta ")
    valor_2 = int(input("Por favor, ingrese su clave ")) 
    contador = contador + 1
    if contador == 3 and valor_2!= valor_ingresado[1]:
        print("Su tarjeta ha sido bloqueada ")
        break
while persona[1]== valor_ingresado[1]and valor_ingresado[2]>0:
    p = (input("Dinero solicitado para sacar :"))
    if p == "Y":
        break
    if int(p)> valor_ingresado[2]:
        print("ingrese un monto dentro del rango permitido ")
    if int(p)<=int(p):
        l = valor_ingresado [2]-int(p)
        valor_ingresado[2]= l
        dinero_total = dinero_total - int(p)
        x =str(valor_ingresado[2])
        y =str(dinero_total)
        lista[0]="saldo cuenta="+ x
        lista[1]="saldo cajero="+ y
        print(lista)
        plata_20=(int(p)//20000)
        plata_10=(int(p)-(plata_20*20000))//10000
        plata_5=((int(p)-(plata_20*20000))%10000)//5000
        dinero20= dinero20 - plata_20
        dinero10= dinero10 - plata_10
        dinero5 = dinero5 - plata_5
        print("billetes 20000=",plata_20)
        print("billetes 10000=",plata_10)
        print("billetes 5000=",plata_5)
