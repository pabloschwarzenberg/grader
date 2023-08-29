def rot13(palabra):
    cifrado = ''
    for i in palabra:
      a = ord(i)
      if (a >= 65 and a <= 90) or (a >=97 and a <= 122):
        if ((a + 13 > 90 and a + 13 <= 103) or (a + 13 > 122 and a + 13 <= 135)):
          cifrado += chr(a -13)
        else:
          cifrado += chr(a + 13)
    return cifrado
        
    
