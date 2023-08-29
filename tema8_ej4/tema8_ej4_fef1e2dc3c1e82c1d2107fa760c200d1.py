def rot13(palabra):
  texto = input("Mensaje cifrado > ").upper()
  abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
  for i in range(28):
      descifrado = ""
      for l in texto:
          if l in abc:
              pos_letra = abc.index(l)
              nueva_pos = (pos_letra - i) % len(abc)
              descifrado += abc[nueva_pos]
          else:
              descifrado+= l
      msj = (f"ROT-{i}:", descifrado)
    return(msj)
    

           