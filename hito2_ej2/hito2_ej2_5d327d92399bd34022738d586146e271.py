a= "A","C","T","G"
def s (adn):
  for i in adn:
    s=a.find(i)
    if s==-1:
      return("cadena invalida")
    else:
      return("valida")

if __name__ == "__main__":
  adn=input("ingrese secuencia: ")
  adn=adn.upper()
  print(s (adn))
  
  





      