def jerigonzo(string):
  vocales="aeiou"
  traduccion=[]
  for a in string:
    if vocales.find(a)==-1:
      traduccion.append(a)
    if vocales.find(a)!=-1:
      traduccion.extend([a,"p",a])
    traduccion_2="".join(traduccion)
  return traduccion_2  
if __name__ == "__main__":
   string=input()
   print(jerigonzo(string))
         