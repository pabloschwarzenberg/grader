#Aprobación de créditos
a = int(input("ingreso (en pesos): "))
b = int(input("año de nacimiento: "))
c = int(input("numero de hijos: "))
d = int(input("años de perseverancia en el banco: "))
e = (input("estados (S: soltero, C: casado):"))
f = (input("si vive en campo o ciudad (U: urbano, R: rural): "))
g = b - 2022

if d and c:
    d >= 10
    c >= 2
    print ("APROBADO")
elif d and c: 
    d <= 9
    c <= 1
    print ("RECHAZADO")

if e and c and g:
    e = "C"
    c > 3
    g = range(45,55)
    print ("APROBADO")
elif e and c and g:
    e = "S"
    c <= 3
    print ("RECHAZADO")

if a and e and f:
    a > 2500000
    e = "S"
    f = "U"
    print ("APROBADO")
elif a and e and f:
    a > 2500000
    e = "S"
    f = "R"
    print ("RECHAZADO")

if a and d:
    a > 3500000
    d > 5
    print("APROBADO")
elif a and d:
    a < 3500000
    d < 5
    print ("RECHAZADO")    

if f and e and c:
    f = "R"
    e = "C"
    c <= 2
    print ("APROBADO")
elif f and e and c:
    f = "U"
    e = "S"
    c > 2
    print ("RECHAZADO")