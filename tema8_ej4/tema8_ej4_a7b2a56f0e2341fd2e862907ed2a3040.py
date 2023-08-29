def rot13(palabra):
  b=list(palabra) 
  for c in b:
      if c==("a"):
        x=int(b.index("a"))
        b[x]=("N")
      elif c=="b":
        x=int(b.index("b"))
        b[x]=("O")
      elif c=="c":
        x=int(b.index("c"))
        b[x]=("P")
      elif c=="d":
        x=int(b.index("d"))
        b[x]=("Q")
      elif c=="e":
        x=int(b.index("e"))
        b[x]=("R")
      elif c=="f":
        x=int(b.index("f"))
        b[x]=("S")
      elif c=="g":
        x=int(b.index("g"))
        b[x]=("T")
      elif c=="h":
        x=int(b.index("h"))
        b[x]=("U")
      elif c=="i":
        x=int(b.index("i"))
        b[x]=("V")
      elif c=="j":
        x=int(b.index("j"))
        b[x]=("W")
      elif c=="k":
        x=int(b.index("k"))
        b[x]=("X")
      elif c=="l":
        x=int(b.index("l"))
        b[x]=("Y")
      elif c=="m":
        x=int(b.index("m"))
        b[x]=("Z")
      elif c=="n":
        j=int(b.index("n"))
        b[j]=("A")
      elif c=="o":
        x=int(b.index("o"))
        b[x]=("B")
      elif c=="p":
        x=int(b.index("p"))
        b[x]=("C")
      elif c=="q":
        x=int(b.index("q"))
        b[x]=("D")
      elif c=="r":
        x=int(b.index("r"))
        b[x]=("E")
      elif c=="s":
        x=int(b.index("s"))
        b[x]=("F")
      elif c=="t":
        x=int(b.index("t"))
        b[x]=("G")
      elif c=="u":
        x=int(b.index("u"))
        b[x]=("H")
      elif c=="v":
        x=int(b.index("v"))
        b[x]=("I")
      elif c=="w":
        x=int(b.index("w"))
        b[x]=("J")
      elif c=="x":
        x=int(b.index("x"))
        b[x]=("K")
      elif c=="y":
        x=int(b.index("y"))
        b[x]=("L")
      elif c=="z":
        x=int(b.index("z"))
        b[x]=("M")
  y="".join(b)
  z=y.lower()
  return(z)
  

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           