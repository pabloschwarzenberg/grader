def rot13(palabra):
  n = 13 
  Lista = list(palabra) 
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
  lstaEncriptada = [] 
  for letra in Lista: 
      if letra.isalpha(): 
          if "A" <= letra <= "Z": 
               lstaEncriptada.append(chr(ord(letra)+n)) 
          else: 
              lstaEncriptada.append(chr((ord(letra)-97+n)%26+97)) 
      elif letra.isdigit(): 
           lstaEncriptada.append(chr((int(letra)+n)%10+48)) 
  i = i+1 
  strEncriptado = "".join(lstaEncriptada) 
  return strEncriptado

if __name__ =="__main__":
  s=input("Escriba algo: ")
  x=rot13(s)
  print(x)