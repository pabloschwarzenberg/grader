def rot13(palabra):
  primero=['a','b','c','d','e','f','g','h','i','j','k','l','m','']
  segundo=['n','o','p','q','r','s','t','u','v','w','x','y','z','']
  nuevapalabra=""
  for _ in palabra:
    if _ in primero:
      posletra = primero.index(_)
      letranueva = segundo[posletra]
      nuevapalabra = nuevapalabra + letranueva
    else:
      posletra = segundo.index(_)
      letranueva = primero[posletra]
      nuevapalabra = nuevapalabra + letranueva
  return nuevapalabra

if __name__=="__main__":
  palabra=input("Ingresa la palabra que quieras encriptar: ")
  palabra.lower()
  resultado=rot13(palabra)
  print("El resultado es: ",resultado)