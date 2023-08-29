def palindromo(palabras):
    if len(palabras)==0 or len(palabras)==1:
        return True
    else:
        if palabras[0]==palabras[len(palabras)-1]:
            palabras=palabras[1:len(palabras)-1]
            #print(palabras)
            return palindromo(palabras)
        else:
            return False

p="oso"
p1="dinosaurio"
frase=[]
for i in range(len(p)):
    if p[i]!=" ":
        frase.append(p[i])

print(palindromo(frase))

frase1=[]
for i in range(len(p1)):
    if p1[i]!=" ":
        frase1.append(p1[i])

print(palindromo(frase1))


#if __name__=="__main__":
 #   print(Palindromo("oso"))
  #  print(Palindromo("dinosaurio"))
           