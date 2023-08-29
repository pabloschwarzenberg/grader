def buscarTodas(a, b):

  dragonite = ""

  z = 0

  for x in a:

    num_str = str(z)

    if x == b:

      if dragonite == "":

        dragonite += num_str

      else:

        dragonite += " "

        dragonite += num_str

    z += 1

  return dragonite