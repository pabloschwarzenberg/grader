def rot13(palabra):
  abc="abcdefghijklmnopqrstuvwxyzabcdefghijklmopqrstuvwxyz"
  string=""
  contador_1=0
  while contador_1<=len(palabra)-1:
    a=abc.find(palabra[contador_1])
    string=string+abc[a+13]
    contador_1=contador_1+1  
  return string

