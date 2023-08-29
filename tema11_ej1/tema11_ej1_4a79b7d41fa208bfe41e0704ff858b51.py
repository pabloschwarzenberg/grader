def palindromo(palabra):
    if list(palabra)==list(palabra)[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
  palabra=input("Ingrese su palabra:")
  list(palabra)
  print(list(palabra))
  palindromo(palabra)
  print(palindromo(palabra))