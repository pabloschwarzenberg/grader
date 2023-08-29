def palindromo(palabra):
  if len(palabra)==1 or len(palabra)==0:
    return True
  else:
      palabra=list(palabra)
      if palabra[0]==palabra[-1]:
          palabra.pop(0)
          palabra.pop(-1)
          "".join(palabra)
          return palindromo(palabra)
      else:
          return False



if __name__ == "__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))