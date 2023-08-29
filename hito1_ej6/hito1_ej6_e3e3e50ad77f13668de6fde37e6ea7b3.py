#Ordenar tres números
numero1= int(input("ingrese primer numero: "))
numero2= int(input("ingrese un segundo numero: "))
numero3= int(input("ingrese un tecer numero: "))
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