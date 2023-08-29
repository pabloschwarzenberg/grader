def d_binario(d):
    if d <= 0:
        return "0"
    b = ""
    while d > 0:
        r = int(d % 2)
        d = int(d / 2)
        b = str(r) + b
    return b
      d= float(input("Ingrese El Numero Que Desea Convertir"))
      b = d_binario(d)
print("Su Numero {d} En Binario Es {b}")