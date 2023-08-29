#Ordenar tres números
print("ingresa 3 numeros")
numero_1 = int(input("Primer numero: "))
numero_2 = int(input("Segundo numero: "))
numero_3 = int(input("tercer numero: "))

mayor = max(numero_1, numero_2, numero_3)
menor = min(numero_1, numero_2, numero_3)
medio = (numero_1 + numero_2 + numero_3) - mayor - menor

print(menor, ",", medio, ",", mayor)
        

        
      