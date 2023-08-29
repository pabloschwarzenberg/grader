#Ordenar tres números

numero_1=int(input("Escribe el primer número:"))
numero_2=int(input("Escribe el segundo número:"))
numero_3=int(input("Escribe el tercer número:"))

if numero_1<= numero_2 <= numero_3 :
    
    print(numero_1,",",numero_2,",",numero_3)
    
elif numero_1<=numero_3<=numero_2:
    
    print(numero_1,",",numero_3,",",numero_2)
    
elif numero_2<=numero_1<=numero_3:
    
    print(numero_2,",",numero_1,",",numero_3)
    
elif numero_2<=numero_3<=numero_1:
    
    print(numero_2,",",numero_3,",",numero_1)
    
elif numero_3<=numero_1<=numero_2:
    
     print(numero_3,",",numero_1,",",numero_2)
     
else:
    
    print(numero_3,",",numero_2,",",numero_1)
    
