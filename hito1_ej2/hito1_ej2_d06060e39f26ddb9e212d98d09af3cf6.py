#Contestador de celular
numero= int(input("Ingrese numero telefonico: "))
cantidadNum=len(str(numero))

while not cantidadNum==8:
    numero= int(input("Ingrese un numero valido: "))
    cantidadNum=len(str(numero))
      
hora= int(input("Ingrese hora de la llamada: "))
cantidadNum2=len(str(hora))

while not cantidadNum2==2:
    hora= int(input("Ingrese una hora valida: "))
    cantidadNum2=len(str(hora))



if hora>=0 and hora<=7:
    print("\nContestar")

var1=numero%1000

if hora<=14 and var1==909:
    print("\nContestar")

if hora<=14 and var1!=909:
    print("\nNo contestar")

var2= int(numero/100000)
print(var2)

if hora>=17 and hora<=19 and var2==877:
    print("\nNo contestar")
    
if hora>=17 and hora<=19 and var2!=877:
    print("\nContestar")

if hora>=19:
    print("\nNo contestar")
         