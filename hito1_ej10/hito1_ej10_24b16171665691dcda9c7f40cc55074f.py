#Cajero Automático
total_del_cajero=1000000
valor_por_el_usuario =[10334151,1803,100000]
x =int(input("Se solicita ingresar el usuario : "))
y =int(input("Se solicita ingresar clave : "))
usuario=[x,y]
contador = 1
lista=[0,0]
while usuario[1]!=valor_por_el_usuario[1] and contador < 3:
    print("La clave ingresada es incorrecta ")
    y = int(input(" Por favor ingrese clave nuevamente :")) 
    contador = contador + 1
    if contador == 3 and y != valor_por_el_usuario[1]:
        print("Su tarjeta ha sido bloqueada ")
        break
while usuario[1]==valor_por_el_usuario[1]and valor_por_el_usuario[2]>0:
    o =(input("Por favor ingrese el monto que desea retirar : "))
    if o == "Y":
        break
    if int(o)>valor_por_el_usuario[2]:
        print("El monto ingresado es incorrecto ")
    if int(o)<=int(o):
        m=valor_por_el_usuario[2]-int(o)
        valor_por_el_usuario[2]=m
        total_del_cajero = total_del_cajero - int(o)
        p = str(valor_por_el_usuario[2])
        i = str(total_del_cajero)
        lista[0]="saldo cuenta="+ p
        lista[1]="saldo cajero="+ i
        print(lista)



