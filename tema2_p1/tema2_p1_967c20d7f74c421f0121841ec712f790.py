# por favor escribe aquí tu función
 numero= int(input("es_primo:"))
 valor = range(2, numero)
 contador = 0
 for n in valor:
    if numero % n == 0:
        contador += 1

 if contador > 0:
    print("False")
 else:
    print("True")
           