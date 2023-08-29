#Ordenar tres números
numero1 = int(input("Ingrese su primer número: "))
    
numero2 = int(input("Ingrese su segundo número: "))
    
numero3= int(input("Ingrese su tercer número: "))
    
menor=min(numero1, numero2, numero3)

mayor=max(numero1, numero2, numero3)

medio=(numero1+numero2+numero3) - menor - mayor

print("El orden es",menor,",", medio ,",", mayor) 