def rot13(palabra):
    
  pi = " abcdefghijklm "
  pf = " nopqrstuvwxyz "
  busc = ""
  p = list(palabra)
  letra = ""
  
  for i in range(len(p)):
      if(p[i] in pi):
          letra = p[i]
          busc = pi.find(letra)
          letra = pf[busc]
          p[i] = letra

      elif(p[i] in pf):
          letra = p[i]
          busc = pf.find(letra)
          letra = pi[busc]
          p[i] = letra

      elif(p[i] == " "):
          pass

  New_p = "".join(p)

  return New_p

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)