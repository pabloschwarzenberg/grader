p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
dine = [33.77,203,27.58,348,51.19]
prod = []
cant = []
mont = []
multi = 1
x = ""
while True:
  x = input("Ingrese: ")
  if x != "ver" and x != "checkout":
    producto = int(x[0])
    cantidad = int(x[2])
    prod.append(producto)
    cant.append(cantidad)
    mont.append(dine[producto - 1])
  if x == "checkout":
    cont = 0
    lista = [1,2,3]
    for i in prod:
      if i in lista:
        cont += 1
        lista.remove(i)
    if cont == 3:
      multi = 0.8

    cont = 0
    lista = [4,5]
    for i in prod:
      if i in lista:
        cont += 1
        lista.remove(i)
    if cont == 2:
      if multi != 0.8 :
        multi = 0.85

    acum = 0
    for i in range(len(prod)):
      acum = acum + (mont[i] * multi * cant[i])
    print(round(acum,1))
    break