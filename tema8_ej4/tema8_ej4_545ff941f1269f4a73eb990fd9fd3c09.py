def rot13(palabra):
  palabra_final=''
  for i in palabra:
    if i=='a':
      palabra_final+='n'
    if i=='b':
      palabra_final+='o'
    if i=='c':
      palabra_final+='p'
    if i=='d':
      palabra_final+='q'
    if i=='e':
      palabra_final+='r'
    if i=='f':
      palabra_final+='s'
    if i=='g':
      palabra_final+='t'
    if i=='h':
      palabra_final+='u'
    if i=='i':
      palabra_final+='v'
    if i=='j':
      palabra_final+='w'
    if i=='k':
      palabra_final+='x'
    if i=='l':
      palabra_final+='y'
    if i=='m':
      palabra_final+='z'
    if i=='n':
      palabra_final+='a'
    if i=='o':
      palabra_final+='b'
    if i=='p':
      palabra_final+='c'
    if i=='q':
      palabra_final+='d'
    if i=='r':
      palabra_final+='e'
    if i=='s':
      palabra_final+='f'
    if i=='t':
      palabra_final+='g'
    if i=='u':
      palabra_final+='h'
    if i=='v':
      palabra_final+='i'
    if i=='w':
      palabra_final+='j'
    if i=='x':
      palabra_final+='k'
    if i=='y':
      palabra_final+='l'
    if i=='z':
      palabra_final+='m'
  return palabra_final
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           