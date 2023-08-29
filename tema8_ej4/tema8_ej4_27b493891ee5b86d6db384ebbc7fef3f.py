def rot13(palabra):
  l = []
  abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
  nop = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
  for a in palabra:
    if a == abc[0]:
      a = nop[0]
      l.append(a)
    elif a == nop[0]:
      a = abc[0]
      l.append(a)

    if a == abc[1]:
      a = nop[1]
      l.append(a)
    elif a == nop[1]:
      a = abc[1]
      l.append(a)

    if a == abc[2]:
      a = nop[2]
      l.append(a)
    elif a == nop[2]:
      l.append(a)

    if a == abc[3]:
      a = nop[3]
      l.append(a)
    elif a == nop[3]:
      a = abc[3]
      l.append(a)

    if a == abc[4]:
      a = nop[4]
      l.append(a)
    elif a == nop[4]:
      a = abc[4]
      l.append(a)

    if a == abc[5]:
      a = nop[5]
      l.append(a)
    elif a == nop[5]:
      l.append(a)

    if a == abc[6]:
      a = nop[6]
      l.append(a)
    elif a == nop[6]:
      a = abc[6]
      l.append(a)

    if a == abc[7]:
      a = nop[7]
      l.append(a)
    elif a == nop[7]:
      a = abc[7]
      l.append(a)

    if a == abc[8]:
      a = nop[8]
      l.append(a)
    elif a == nop[8]:
      a = abc[8]
      l.append(a)

    if a == abc[9]:
      a = nop[9]
      l.append(a)
    elif a == nop[9]:
      a = abc[9]
      l.append(a)

    if a == abc[10]:
      a = nop[10]
      l.append(a)
    elif a == nop[10]:
      a = abc[10]
      l.append(a)

    if a == abc[11]:
      a = nop[11]
      l.append(a)
    elif a == nop[11]:
      a = abc[11]
      l.append(a)

    if a == abc[12]:
      a = nop[12]
      l.append(a)
    elif a == nop[12]:
      a = abc[12]
      l.append(a)
  return "".join(l)
  
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           