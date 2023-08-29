def jerigonzo(palabra):
   lista = list(palabra)
   contador = 0
   resultado = ""
   for a in palabra:
     if lista[contador] == "a":
       resultado += "apa"
     elif lista[contador] == "e":
       resultado += "epe"
     elif lista[contador] == "i":
       resultado += "ipi"
     elif lista[contador] == "o":
       resultado += "opo"
     elif lista[contador] == "u":
       resultado += "upu"
     else:
       resultado += lista[contador]
     contador += 1
   
   return resultado

if __name__ == "__main__": 
  pNormal=input()
  print(jerigonzo(pNormal))
       
     
     
     