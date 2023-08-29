def rot13(palabra):
  nueva_palabra = ''
  for i in palabra: 
    if ord(i) <= 109: 
      num = int(ord(str(i)))+13
      nueva_palabra += chr(num)
    else:
      num = int(ord(i))-13
      nueva_palabra += chr(num)
  return(nueva_palabra)