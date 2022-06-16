import random

while True:
  aleatorio = random.randrange(0, 3)
  elijePc =""
  print("1. Piedra")
  print("2. Papel")
  print("3. Tijera")
  opcion = int(input("Elige tu opcion"))

  
  print("Elejiste:", usuario)

  if aleatorio ==0:
    elijepc = "Piedra"
  elif aleatorio ==1:
    elijePc = "Papel"
  elif aleatorio ==2:
    elijePc = "Tijera"
  print("La maquina elijio: ", elijePc)
  print("...")
  if elijePc == "piedra" and usuario == "Papel":
    print("Ganaste, papel envuelve tijera")
  elif elijePc == "Papel" and usuario == "Tijera":
    print("Ganaste, Tireja corta papel")
  elif elijePc == "Tijera" and usuario == "Piedra":
    print("Ganaste, Piedra  machaca Tijera")
  if elijePc == "Papel" and usuario == "Piedra":
    print("Perdiste, Papel envuelve Piedra")
  elif elijePc == "Tijera" and usuario == "Papel":
    print("Perdiste, Tireja corta Papel")
  elif elijePc == "Piedra" and usuario == "Tijera":
    print("Perdiste, Piedra machaca Tijera")
  elif elijePc == usuario:
    print("Empate")