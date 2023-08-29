def rot13(frase):
  n = 13 #2
  Lista = list(frase) #3
  i = 0 #5
  for letra in Lista: #6
      if letra == "á": #7
          Lista[i] = "a" #8
      elif letra == "é": #9
          Lista[i] = "e" #10
      if letra == "í": #11
          Lista[i] = "i" #12
      elif letra == "ó": #13
          Lista[i] = "o" #14
      elif letra == "ú": #15
          Lista[i] = "u" #16
      elif letra == "Á": #17
          Lista[i] = "A" #18
      elif letra == "É": #19
          Lista[i] = "E" #20
      elif letra == "Í": #21
          Lista[i] = "I" #22
      elif letra == "Ó": #23
          Lista[i] = "O" #24
      elif letra == "Ú": #25
          Lista[i] = "U" #26
      i = i+1 #27
  lstEncriptada = [] #28
  for letra in Lista: #29
      if letra.isalpha(): #30
          if "A" <= letra <= "Z": #31
               lstEncriptada.append(chr(ord(letra)+n)) #32
          else: #33
              lstEncriptada.append(chr((ord(letra)-97+n)%26+97)) #34
      elif letra.isdigit(): #35
           lstEncriptada.append(chr((int(letra)+n)%10+48)) #36
  i = i+1 #37
  strEncriptado = "".join(lstEncriptada) #38
  return strEncriptado #39 

if __name__ =="__main__":
  s=input("Escriba algo: \n")
  x=rot13(s)
  print(x)