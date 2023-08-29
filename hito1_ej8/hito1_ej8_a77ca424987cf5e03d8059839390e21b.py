#Descomponer un número
numero =int(input("Ingresa un numero: "))
if numero>999:
    u= int(numero%10**1)
    d=numero%10**2//10**1
    c=numero%10**3//10**2
    m=numero//10**3
    print(m, "M+", c, "C+", d, "D+", u, "U")
if numero<1000:
    u= numero%10**1
    d=numero%10**2//10**1
    c=numero//10**2
    print(c, "C+", d, "D+", u, "U")
if numero<100:
    u= numero%10**1
    d=numero//10**1
    print(d, "D+", u, "U")
if numero<10:
    u = numero
    print(u, "U")