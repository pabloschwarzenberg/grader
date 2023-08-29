def decodificar(mensaje):
    lista=mensaje.split(sep=",")

    a=int(lista[0][0])*2**7
    b=int(lista[0][1])*2**6
    c=int(lista[0][2])*2**5
    d=int(lista[0][3])*2**4
    e=int(lista[0][4])*2**3
    f=int(lista[0][5])*2**2
    g=int(lista[0][6])*2**1
    h=int(lista[0][7])*2**0

    i=int(lista[1][0])*2**7
    j=int(lista[1][1])*2**6
    k=int(lista[1][2])*2**5
    l=int(lista[1][3])*2**4
    m=int(lista[1][4])*2**3
    n=int(lista[1][5])*2**2
    o=int(lista[1][6])*2**1
    p=int(lista[1][7])*2**0

    q=int(lista[2][0])*2**7
    r=int(lista[2][1])*2**6
    s=int(lista[2][2])*2**5
    t=int(lista[2][3])*2**4
    u=int(lista[2][4])*2**3
    v=int(lista[2][5])*2**2
    w=int(lista[2][6])*2**1
    x=int(lista[2][7])*2**0

    y=int(lista[3][0])*2**7
    z=int(lista[3][1])*2**6
    A=int(lista[3][2])*2**5
    B=int(lista[3][3])*2**4
    C=int(lista[3][4])*2**3
    D=int(lista[3][5])*2**2
    E=int(lista[3][6])*2**1
    F=int(lista[3][7])*2**0

    letrauno=a+b+c+d+e+f+g+h
    letrados=i+j+k+l+m+n+o+p
    letratres=q+r+s+t+u+v+w+x
    letracuatro=y+z+A+B+C+D+E+F

    palabra=chr(letrauno), chr(letrados), chr(letratres), chr(letracuatro)
    mensaje=''.join(palabra)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         