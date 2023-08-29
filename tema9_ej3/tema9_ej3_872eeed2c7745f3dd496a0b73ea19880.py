def decodificar(mensaje):

    l=mensaje.split(",")

    i=0

    l_letras=[]

    while i<len(l):

        s=l[i]

        x=0

        decimal=0

        while x<len(s):

            n=s[x]
            n=int(n)

            lar=len(s)

            lar=int(lar)

            dec=(2**(lar-1-x))*n

            decimal=decimal+dec

            letra=chr(decimal)

            x=x+1

        l_letras.append(letra)


        i=i+1

    mean="".join(l_letras)


    return mean

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         