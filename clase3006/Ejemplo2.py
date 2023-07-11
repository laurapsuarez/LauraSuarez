def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1 or n > 5:
                print("Error ingrese un estrato valido (1 a 5)")
                input("digite cualquier tecla para continuar")
                continue
            return n
        except ValueError:
            print("Error  ingrese un numero entero valido.")
  
def leerString(msg):
    while True:
        try: 
            s = input(msg)
            if s == "" or s.strip() == " ":
                print("no ingrese un campo vacio")
                input("digite cualquier nombre para continuar")
                continue
            return s
        except Exception as e:
            print("error al ingresar un nombre",e.message)
   
def serviEnergia(estrato):
    if estrato == 1:
        return 10_000
    elif estrato == 2:
        return 15_000
    elif estrato == 3:
        return 30_000
    elif estrato == 4:
        return 50_000
    elif estrato == 5:
        return 65_000  
   
nombre = leerString("Ingrese el nombre: ")
estrato = leerInt("Ingrese el estrato: ")
tarifa = serviEnergia(estrato)

print(f"LA TARIFA BASICA DE ENERGIA DE {nombre} ES DE ${tarifa:,}")