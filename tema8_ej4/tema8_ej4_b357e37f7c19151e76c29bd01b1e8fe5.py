def rot13(palabra):
  palabra_=[] 
  abecedario_1=['a','b','c','d','e','f','g','h','i','j','k','l','m']
  abecedario_2=['n','o','p','q','r','s','t','u','v','w','x','y','z']
  for i in palabra:
    Encriptado=''
    if i in abecedario_1:
      palabra_.append(abecedario_2[abecedario_1.index(i)])
      Encriptado=Encriptado+''.join(palabra_)
    else:
      palabra_.append(abecedario_1[abecedario_2.index(i)])
      Encriptado=Encriptado+''.join(palabra_)

  return Encriptado