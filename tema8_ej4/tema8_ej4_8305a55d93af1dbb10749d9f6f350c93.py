def rot13(palabra):
  cambios=0
  while cambios != len(palabra):
    if "a" in palabra:
      veces=palabra.count("a")
      palabra=palabra.replace("a","N")
      cambios=cambios+veces
    if "b" in palabra:
      veces=palabra.count("b")
      palabra=palabra.replace("b","O")
      cambios=cambios+veces
    if "c" in palabra:
      veces=palabra.count("c")
      palabra=palabra.replace("c","P")
      cambios=cambios+veces
    if "d" in palabra:
      veces=palabra.count("d")
      palabra=palabra.replace("d","Q")
      cambios=cambios+veces
    if "e" in palabra:
      veces=palabra.count("e")
      palabra=palabra.replace("e","R")
      cambios=cambios+veces
    if "f" in palabra:
      veces=palabra.count("f")
      palabra=palabra.replace("f","S")
      cambios=cambios+veces
    if "g" in palabra:
      veces=palabra.count("g")
      palabra=palabra.replace("g","T")
      cambios=cambios+veces
    if "h" in palabra:
      veces=palabra.count("h")
      palabra=palabra.replace("h","U")
      cambios=cambios+veces
    if "i" in palabra:
      veces=palabra.count("i")
      palabra=palabra.replace("i","V")
      cambios=cambios+veces
    if "j" in palabra:
      veces=palabra.count("j")
      palabra=palabra.replace("j","W")
      cambios=cambios+veces
    if "k" in palabra:
      veces=palabra.count("k")
      palabra=palabra.replace("k","X")
      cambios=cambios+veces
    if "l" in palabra:
      veces=palabra.count("l")
      palabra=palabra.replace("l","Y")
      cambios=cambios+veces
    if "m" in palabra:
      veces=palabra.count("m")
      palabra=palabra.replace("m","Z")
      cambios=cambios+veces
    if "n" in palabra:
      veces=palabra.count("n")
      palabra=palabra.replace("n","A")
      cambios=cambios+veces
    if "o" in palabra:
      veces=palabra.count("o")
      palabra=palabra.replace("o","B")
      cambios=cambios+veces
    if "p" in palabra:
      veces=palabra.count("p")
      palabra=palabra.replace("p","C")
      cambios=cambios+veces
    if "q" in palabra:
      veces=palabra.count("q")
      palabra=palabra.replace("q","D")
      cambios=cambios+veces
    if "r" in palabra:
      veces=palabra.count("r")
      palabra=palabra.replace("r","E")
      cambios=cambios+veces
    if "s" in palabra:
      veces=palabra.count("s")
      palabra=palabra.replace("s","F")
      cambios=cambios+veces
    if "t" in palabra:
      veces=palabra.count("t")
      palabra=palabra.replace("t","G")
      cambios=cambios+veces
    if "u" in palabra:
      veces=palabra.count("u")
      palabra=palabra.replace("u","H")
      cambios=cambios+veces
    if "v" in palabra:
      veces=palabra.count("v")
      palabra=palabra.replace("v","I")
      cambios=cambios+veces
    if "w" in palabra:
      veces=palabra.count("w")
      palabra=palabra.replace("w","J")
      cambios=cambios+veces
    if "x" in palabra:
      veces=palabra.count("x")
      palabra=palabra.replace("x","K")
      cambios=cambios+veces
    if "y" in palabra:
      veces=palabra.count("y")
      palabra=palabra.replace("y","L")
      cambios=cambios+veces
    if "z" in palabra:
      veces=palabra.count("z")
      palabra=palabra.replace("z","M")
      cambios=cambios+veces
   
              
              
    
    
    return palabra.lower()


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)