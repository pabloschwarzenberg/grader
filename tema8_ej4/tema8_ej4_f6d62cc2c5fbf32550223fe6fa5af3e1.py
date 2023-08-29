def rot13(n):
    a=""
    desplazamiento=13
    letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(len(a)):
        for x in range(len(letras)):
            if n[i]==letras[x]:
               if x + desplazamiento > 25:
                  diff=(x + desplazamiento)-25
                  a=a+(letras[diff-1])
               else:
                  a=a+(letras[x+desplazamiento])
                  return a