n = int(input("ingrese un numero positivo: "))
suma = 0
contador = 1

while contador != n:
    if n%contador == 0:
        suma = suma + contador
    contador = contador + 1
    
if suma == n:
    print(f"{n} es un numero dado perfecto")
else:
    print(f"{n} no es un dado perfecto")