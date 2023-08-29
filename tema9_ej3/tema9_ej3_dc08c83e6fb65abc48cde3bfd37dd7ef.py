def bin_dec(numero):
    largo=len(numero)
    i=0
    entero=0
    while i<largo:
        potencia=2**(largo-i-1)
        digito=int(numero[i])
        entero=entero+digito*potencia
        i=i+1
    return entero
    
    
def decodificar(mensaje):
    mensaje=mensaje.split(",")
    m_f=[]
    for palabra in mensaje:
      numero=bin_dec(palabra)
      letra=chr(numero)
      m_f.append(letra)
    m_f="".join(m_f)  
    return m_f

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print("hola")
         