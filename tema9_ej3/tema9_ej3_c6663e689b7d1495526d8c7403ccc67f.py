def abinario(string):
    x=list(string)
    x.reverse()
    total=0
    exp=0
    for i in x:
        w=(2**exp)*int(i)
        total+=w
        exp+=1
    return(total)
def decodificar(mensaje):
    output=""
    mensaje=mensaje.split(",")
    for i in mensaje:
        x=abinario(i)
        x=chr(x)
        output+=x
    return(output)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         