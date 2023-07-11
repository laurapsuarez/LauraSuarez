def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Error!  ingrese un numero entero valido.")

def leerString(msg):
    while True:
        try: 
            s = input(msg)
            if s == "" or s.strip() == " " or len(s) != 1:
                print("ingrese un campo valido")
                input("digite cualquier nombre para continuar")
                continue
            return s
        except Exception as e:
            print("error al ingresar un nombre",e.message)

canLetras = leerInt("ingrese el numero de letras que desea ingresar: ")
lstLetras = []
for i in range (canLetras):
    letra = leerString("ingrese una letra: ")
    letra = letra.upper()
    lstLetras.append(letra)
    #print(lstLetras)

a = lstLetras.count("A")
e = lstLetras.count("E")
i = lstLetras.count("I")
o = lstLetras.count("O")
u = lstLetras.count("U")

print(f"la vocal a esta presente {a} veces")
print(f"la vocal e esta presente {e} veces")
print(f"la vocal i esta presente {i} veces")
print(f"la vocal o esta presente {o} veces")
print(f"la vocal u esta presente {u} veces")