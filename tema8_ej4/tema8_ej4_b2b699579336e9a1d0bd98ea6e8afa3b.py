def rot13(mensaje):
  abc="abcdefghijklmnopqrstuvwxyz"
  m_encr=""
  lista_pos=[]
  for i in mensaje:
      for j in range(len(abc)):
          if j <=12:
              if i==abc[j]:
                m_encr=m_encr+abc[j+13]
          elif j>12:
            if i==abc[j]:
                m_encr=m_encr+abc[j-13]
  return(m_encr)

        

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           