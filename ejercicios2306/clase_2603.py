# numero pares de uno a 100

# for i in range(2,101,2):
#     print(i, end=",")

# hacer un programa que calcule el factorial de un numero
# n = int(input("ingrese un numero: "))
# fact = 1
# for i in range (1,n+1):
#     fact = fact * i
# print(fact)

# Ejercicio 3
# determinar e imprimir si un numero es primo o no

n = int(input("ingrese un numero: "))
primo = True
culpable = 0
for i in range (2,n):
    if n%i == 0:
        primo = False
        culpable = 1
if primo:
    print(f"{n} es primo")
else:
    print(f"{n} no es primo")
    