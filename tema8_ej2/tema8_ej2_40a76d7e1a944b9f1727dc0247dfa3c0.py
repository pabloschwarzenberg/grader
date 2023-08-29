"""
Programa una función llamada buscarTodas(a,b), 
que encuentre todas las apariciones del string b en el string a, 
y retorne un string que representa a una secuencia de índices separada por espacios. 
Por ejemplo, al ejecutar buscarTodas(’tres tristes tigres’,’t’), 
debería retornar el string ’0 5 9 13’ (no hay espacios después del número 13).
"""

def buscarTodas(palabra,letra):
    contador_t=""
    for i,l in enumerate(palabra):
        if l==letra:
            print(i)
            contador_t=contador_t+str(i)+" "
    return contador_t.rstrip()

if __name__ == "__main__":
    palabra=str(input("ingrese palabra: "))
    letra=str(input("ingrese letra: "))
    print(buscarTodas(palabra,letra))