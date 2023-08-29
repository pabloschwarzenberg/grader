def rot13(x):
  a = []
  x_l = list(x)
  pos = 0
  for carac in x_l:
        asci = ord(carac)
        if asci >= 97 and asci <= 109:
            a.append(str(chr(asci+13)))
        elif asci >= 110 and asci <= 122:
            a.append(str(chr(asci-13)))
        else:
            a.append(str(chr(asci)))
        pos += 1        
  return "".join(a)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           