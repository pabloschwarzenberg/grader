def rot13(palabra): 
  lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
  listb = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
  listc = []

  for i in palabra:
    if i == lista[0]:
      listc.append(listb[0])
    elif i == lista[1]:
      listc.append(listb[1])
    elif i == lista[2]:
      listc.append(listb[2])
    elif i == lista[3]:
      listc.append(listb[3])
    elif i == lista[4]:
      listc.append(listb[4])
    elif i == lista[5]:
      listc.append(listb[5])
    elif i == lista[6]:
      listc.append(listb[6])
    elif i == lista[7]:
      listc.append(listb[7])
    elif i == lista[8]:
      listc.append(listb[8])
    elif i == lista[9]:
      listc.append(listb[9])
    elif i == lista[10]:
      listc.append(listb[10])
    elif i == lista[11]:
      listc.append(listb[11])
    elif i == lista[12]:
      listc.append(listb[12])

    if i == listb[0]:
      listc.append(lista[0])
    elif i == listb[1]:
      listc.append(lista[1])
    elif i == listb[2]:
      listc.append(lista[2])
    elif i == listb[3]:
      listc.append(lista[3])
    elif i == listb[4]:
      listc.append(lista[4])
    elif i == listb[5]:
      listc.append(lista[5])
    elif i == listb[6]:
      listc.append(lista[6])
    elif i == listb[7]:
      listc.append(lista[7])
    elif i == listb[8]:
      listc.append(lista[8])
    elif i == listb[9]:
      listc.append(lista[9])
    elif i == listb[10]:
      listc.append(lista[10])
    elif i == listb[11]:
      listc.append(lista[11])
    elif i == listb[12]:
      listc.append(lista[12])

  cadena ="".join(listc)
  return cadena
           