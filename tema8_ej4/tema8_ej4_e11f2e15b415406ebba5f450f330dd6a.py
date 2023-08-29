def rot13(texto):
    upc = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM"
    lowc = "abcdefghijklmnopqrstuvwxyzabcdefghijklm"
    r13 = ""
    for l in texto :
      if l in upc:
        r13 = r13 + upc[upc.find(l)+13]
      elif l in lowc :
        r13 = r13 + lowc[lowc.find(l)+13]
      else:
        r13 = r13 + l
    return r13


           