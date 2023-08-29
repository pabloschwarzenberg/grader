def binario(mensaje):
    mensaje=mensaje.split(",")
    binario=[]
    for i in range (len(mensaje)):
        numero=int(mensaje[i])
        a=(numero%10)*1
        b=numero//10
        c=(b%10)*2
        d=b//10
        e=(d%10)*4
        f=d//10
        g=(f%10)*8
        h=f//10
        t=(h%10)*16
        y=h//10
        j=(y%10)*32
        u=y//10
        i=(u%10)*64
        o=u//10
        p=(o%10)*128
        x=o//10
        s=(x%10)*256
        suma=s+p+i+j+t+g+e+c+a
        binario.append(str(suma))
    return binario
def decodificar(mensaje2):
    j=0
    string=""
    while j<len(mensaje2):
      elemento=mensaje2[j]
      if elemento==",":
        string=string
        j=j+1
      else:
        binario=int(elemento)
        binario_letra=chr(binario)
        string=string+binario_letra
        j=j+1        
    return"hola"

if __name__ == "__main__":
  mensaje1=binario("01101000,01101111,01101100,01100001")
  mensaje2=decodificar(mensaje1)
  print(mensaje2)


         