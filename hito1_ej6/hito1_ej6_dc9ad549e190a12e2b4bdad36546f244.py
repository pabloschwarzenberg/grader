#Ordenar tres números
a = int (input("Escriba el primer numero:"))    
b = int (input("Escriba el segundo numero:")) 
c = int (input("Escriba el tercer numero:")) 
Ma = max(a, b, c)
Mi = min(a, b, c) 
D = (a + b + c) - Ma - Mi
print ("Los numeros ordenados son:",Mi ,",", D , ",",Ma)