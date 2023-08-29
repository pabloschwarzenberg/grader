#Ordenar tres números
numero1= int(input("ingresar el primer número: "))
numero2= int(input("ingresar el segundo número: "))
numero3= int(input("ingresar el tecer número: "))

if numero1 <= numero2 <= numero3:
    secuencia= numero1 , numero2, numero3
elif numero2 <= numero1 <=numero3:
    secuencia= numero2 , numero1 , numero3 
elif numero3 <= numero2 <= numero1:
    secuencia= numero3 , numero2, numero1
elif numero2 <= numero3 <= numero1:
    secuencia= numero2 , numero3 , numero1
elif numero3 <= numero1 <= numero2:
    secuencia= numero3 , numero1 , numero2
elif numero1 <= numero3 <= numero2:
    secuencia= numero2 , numero3 , numero1
print(" los numeros de menor a mayor son: ", {secuencia})