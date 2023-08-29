#Contestador de celular
n=input()
h=int(input())

#n[inicio:termino:cada cuanto]
inicio=int(n[0:3])
termino=int(n[4:8])

if 0<h<7:
    print("CONTESTAR")

elif 7<=h<14:
    if termino==909:
        print("NO CONTESTAR")
    
    else:
        print("CONTESTAR")

elif 14<=h<17:
    print("NO CONTESTAR")

elif 17<=h<19:
    if inicio==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

elif 19<=h<23:
    print("NO CONTESTAR")