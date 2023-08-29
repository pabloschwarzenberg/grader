#Ordenar tres números
a = int(input("Ingrese un número de igual cantidad de dígitos:   "))
b = int(input("Ingrese un número de igual cantidad de dígitos:   "))
c = int(input("Ingrese un número de igual cantidad de dígitos:   "))

if a < b < c : 
    print("Ordenados de manera ascendente:"  + str(a) + "," + str(b) + "," + str(c))
elif a < c < b : 
    print("Ordenados de manera ascendente:"  + str(a) + "," + str(c) + "," + str(b))
elif b < a < c : 
    print("Ordenados de manera ascendente:"  + str(b) + "," + str(a) + "," + str(c))
elif b < c < a : 
    print("Ordenados de manera ascendente:"  + str(b) + "," + str(c) + "," + str(a))
elif c < a < b : 
    print("Ordenados de manera ascendente:"  + str(c) + "," + str(a) + "," + str(b))
elif c < b < a : 
    print("Ordenados de manera ascendente:"  + str(c) + "," + str(b) + "," + str(a))
    
elif a == b < c : 
    print("Ordenados de manera ascendente:"  + str(a) + "," + str(b) + "," + str(c))
elif a == c < b : 
    print("Ordenados de manera ascendente:"  + str(a) + "," + str(c) + "," + str(b))
elif b == a < c : 
    print("Ordenados de manera ascendente:"  + str(b) + "," + str(a) + "," + str(c))
elif b == c < a : 
    print("Ordenados de manera ascendente:"  + str(b) + "," + str(c) + "," + str(a))
elif c == a < b : 
    print("Ordenados de manera ascendente:"  + str(c) + "," + str(a) + "," + str(b))
elif c == b < a : 
    print("Ordenados de manera ascendente:"  + str(c) + "," + str(b) + "," + str(a))
    
elif a < b == c : 
    print("Ordenados de manera ascendente:"  + str(a) + "," + str(b) + "," + str(c))
elif a < c == b : 
    print("Ordenados de manera ascendente:"  + str(a) + "," + str(c) + "," + str(b))
elif b < a == c : 
    print("Ordenados de manera ascendente:"  + str(b) + "," + str(a) + "," + str(c))
elif b <c == a : 
    print("Ordenados de manera ascendente:"  + str(b) + "," + str(c) + "," + str(a))
elif c <a == b : 
    print("Ordenados de manera ascendente:"  + str(c) + "," + str(a) + "," + str(b))
elif c < b == a : 
    print("Ordenados de manera ascendente:"  + str(c) + "," + str(b) + "," + str(a))
    
