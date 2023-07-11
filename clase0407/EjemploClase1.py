# hacer una programa que le ayude a un profesor que tiene
# un profesor ingresa la not que tiene el programa le muestra el
# promedio, la nota mayor, la nota menor y las tres primeras notas de mayor a menor


def leerFloat(msg):
    while True:
        try:
            n = float(input(msg))
            if n < 0 or n > 5:
                print("ingrese un valor valido (0 a 5)")
                input("digite cualquier tecla para continuar")
                continue
            return n
        except ValueError:
            print("Error!  ingrese un numero entero valido.")


lstNotas = []

for est in range(1,11):
    nota = leerFloat(f"ingrese nota del estudiante #{est}: ")
    lstNotas.append(nota)
    
notMen = min(lstNotas)
notMayor = max(lstNotas)

promNotas = sum(lstNotas) / 10

lstNotas.sort(reverse=True)
tresNotas = lstNotas[0:3]

print("*" * 30)
print(f"la nota menor fue >> {notMen}")
print(f"la nota mayor fue >> {notMayor}")
print(f"el promedio fue >> {promNotas}")
print(f"las tres primeras notas son {tresNotas}")
print("*" * 30)