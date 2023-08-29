def rot13(s):
    chart = "abcdefghijklmnopqrstuvwxyz"
    tradu = chart[13:]+chart[:13]
    rot_chart = lambda c: tradu[chart.find(c)] if chart.find(c)>-1 else c
    return ''.join( rot_chart(c) for c in s )
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)

