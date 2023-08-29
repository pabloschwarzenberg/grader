def Secuencia(adn):
    adn = str(adn.upper())
    Genoma = ["A", "C", "T", "G"]
    Gcantidad = 0

    for i in adn:

        if i in Genoma:
            Gcantidad += 1

        if Gcantidad == len(adn):
            return True

        if i not in Genoma:
            return False


def secuencia2(l, n):

    secuencia_separada=[]
    l = l.lower()

    if len(l) % n != 0:

        return "ninguna"

    else:

        b = 0

        while b * n < len(l):
            f = str(l[b * n:(b + 1) * n])
            secuencia_separada.append(f)
            b += 1

    return secuencia_separada
    
if __name__ == "__main__":

  x = input("Ingresar secuencia de adc para verificar si es correcta: ")
  m = int(input("De a cuantas letras desea separar la secuencia? (Que sea divisible)"))

  if Secuencia(x) is True:
  
      print("secuencia correcta")

  print(secuencia2(x,m))


