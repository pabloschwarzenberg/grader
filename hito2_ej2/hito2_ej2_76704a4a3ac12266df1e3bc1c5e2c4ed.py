sec=input("tu adn: ")
may=sec.upper()

a=may.count("A")
t=may.count("T")
g=may.count("G")
c=may.count("C")
suma=a+t+c+g
if suma==len(may):
    print("secuencia correcta")
else:
    print("secuencia incorrecta")
  