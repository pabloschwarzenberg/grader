#Descomponer un número

numero=int(input('Ingrese un número entero de hasta 4 dígitos: '))

numeroTexto=(str(numero))
numeroLargo=len(numeroTexto)
while numeroLargo>4:
    numero=int(input('Ingrese un número entero de hasta 4 dígitos: '))

if numeroLargo==4:
    mil=numero//1000
    numero=numero%1000

    centena=numero//100
    numero=numero%100
    
    decena=numero//10

    unidad=numero%10

    print(mil,'M',' + ',centena,'C', ' + ',decena,'D', ' + ',unidad,'U')
    
  
if numeroLargo==3:
    centena=numero//100
    numero=numero%100

    decena=numero//10
    
    unidad=numero%10
    
    print(centena,'C', ' + ',decena,'D', ' + ',unidad,'U')

 
if numeroLargo==2:
    decena=numero//10
    
    unidad=numero%10

    print(decena,'D', ' + ',unidad,'U')

    
if numeroLargo==1:

    print(numero,'U')