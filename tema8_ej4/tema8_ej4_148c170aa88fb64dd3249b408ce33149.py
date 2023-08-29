def rot13(s):
    abcdario = "abcdefghijklmnopqrstuvwxyz"
    transformar = abcdario[13:]+abcdario[:13]
    rot_change = lambda c: transformar[abcdario.find(c)] if abcdario.find(c)>-1 else c
    return ''.join( rot_change(c) for c in s )
if __name__=="__main__":
  incriptar=input("Ingrese el mensaje que desee incriptar:")
  print(rot13(incriptar))