def rot13(frase):
  n = 13
  Lista = list(frase)
  i = 0
  for letra in Lista:
      if letra == "á": 
          Lista[i] = "a"
      elif letra == "é": 
          Lista[i] = "e" 
      if letra == "í": 
          Lista[i] = "i" 
      elif letra == "ó": 
          Lista[i] = "o" 
      elif letra == "ú": 
          Lista[i] = "u" 
      elif letra == "Á": 
          Lista[i] = "A" 
      elif letra == "É": 
          Lista[i] = "E" 
      elif letra == "Í": 
          Lista[i] = "I" 
      elif letra == "Ó": 
          Lista[i] = "O" 
      elif letra == "Ú": 
          Lista[i] = "U" 
      i = i+1 
  lstEncriptada = [] 
  for letra in Lista: 
      if letra.isalpha(): 
          if "A" <= letra <= "Z": 
               lstEncriptada.append(chr(ord(letra)+n)) 
          else: 
              lstEncriptada.append(chr((ord(letra)-97+n)%26+97)) 
      elif letra.isdigit(): 
           lstEncriptada.append(chr((int(letra)+n)%10+48)) 
  i = i+1 
  strEncriptado = "".join(lstEncriptada) 
  return strEncriptado  

if __name__ =="__main__":
  s=input("Escriba algo: \n")
  x=rot13(s)
  print(x)