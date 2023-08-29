numero1=int(input ("ingrese numero uno: " ))
numero2=int(input ("ingrese numero dos: " ))
numero3=int(input ("ingrese numero tres: " ))
sumatoria= numero1+numero2+numero3
numeromayor= max (numero1, numero2, numero3)
numeromenor= min (numero1, numero2, numero3)
numeromedio= sumatoria - (numeromayor + numeromenor)
resultado= (numeromenor,numeromedio, numeromayor)
print(resultado)   