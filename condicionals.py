datoA = int(input("ingresa un numero:"))
datoB = int(input("ingresa otro numero: "))
datoC = int(input("ingresa un tercer numero: "))

if datoA > datoB:
      if datoA > datoC:
            print("El mayor numero es: ", datoA)
      else:
            print("El mayor numero es: ", datoC)
else:
      if datoB > datoC:
            print("El mayor numero es: ", datoB)
      else:
            print("El mayor numero es: ", datoC)
