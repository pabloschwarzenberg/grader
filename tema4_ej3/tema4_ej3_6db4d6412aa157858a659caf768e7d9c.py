def jerigonzo(palabra):
  palabraNueva=""
  for letra in palabra:
      if letra=="a" or letra=="á":
          palabraNueva = palabraNueva + "apa"

      elif letra=="e" or letra=="é":
          palabraNueva = palabraNueva + "epe"

      elif letra=="i" or letra=="í":
          palabraNueva = palabraNueva + "ipi"

      elif letra=="o" or letra=="ó":
          palabraNueva = palabraNueva + "opo"

      elif letra=="u" or letra=="ú":
          palabraNueva = palabraNueva + "upu"

      else:
          palabraNueva=palabraNueva + letra
  return palabraNueva

if __name__ == "__main__":
    print(jerigonzo(input()))