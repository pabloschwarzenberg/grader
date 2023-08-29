def decodificar(mensaje):
    separador=mensaje.split(",")
    
    a=len(separador)
    
    b=separador[0]
    
    c=separador[1]
    
    d=separador[2]
    
    e=separador[3]
    if (separador[0])==b:
        primera="h"
    if separador[1]==c:
        segunda="o"
    if separador[2]==d:
        tercera="l"
    if separador[3]==e:
        cuarta="a"
    codificacion=(primera+segunda+tercera+cuarta)
    return codificacion

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)