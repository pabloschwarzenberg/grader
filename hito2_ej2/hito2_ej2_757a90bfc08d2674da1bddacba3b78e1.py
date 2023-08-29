a = str(input("Ingrese secuencia del adn: "))

x = 0
c = a.upper()
c = list(c)
v = ["A", "C", "T", "G"]
y = len(c)
for l in c:
    for ñ in v:
        if l == ñ:
            x= x+1
        else:
            x= x+0

if x == y:
    print("La secuencia ",a,"es correcta")
else:
    print("La secuencia ",a,"es incorrecta")
    