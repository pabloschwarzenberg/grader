cantidad = 0
numeros= []
promedio = 0
minimo = 0

while True:
    num = float(input("ingrese numero"))
    if num == '':
       print("promedio","=","nd")
       print("minimo","=","nd")
       print("cantidad","=","0")

       
       
    if num == '-1':
      break
    numeros.append(num)
    print(numeros)
    cantidad=cantidad+1
    print("cantidad","=",cantidad)

    if cantidad > 0:
        print("promedio","=",round(sum(numeros)/len(numeros),1))
        print("minimo","=",min(numeros))



