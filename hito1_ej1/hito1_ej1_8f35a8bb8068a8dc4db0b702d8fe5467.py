print("Sea: \nPT=Tareas \nPI=Interrogaciones \nNE=Examen \nPP=presentación \n")

pt = eval(input("Ingrese PT: "))
pi = eval(input("Ingrese PI: "))
ne = eval(input("Ingrese NE: "))
pp = eval(input("Ingrese PP: "))

a = 0.3 * pt
b = 0.3 * pi
c = 0.3 * ne
d = 0.1 * pp

num = a + b + c + d
round(num,1)

print ("El promedio final es: ",num)
      