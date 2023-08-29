def mcm(a, b, ab):
    division = a // b
    resto = a % b
    if resto == 0:
      resultado =ab /b
      return resultado
    else:
       bresto=b*resto
       x=mcm(b, resto,bresto )

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    ab = a * b
    mcm = mcm(a, b, ab)
    print(mcm)