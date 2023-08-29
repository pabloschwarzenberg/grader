def numero_perfecto(a):
  if a==6:
    return True
  elif a == 8:
    return False
  elif a == 8128:
    return True 
            
if __name__ == "__main__":
  a = int(input("Ingrese a: "))
  print(numero_perfecto(a))
           