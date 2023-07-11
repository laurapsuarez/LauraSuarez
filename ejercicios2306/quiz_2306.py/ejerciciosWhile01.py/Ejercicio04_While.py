n = 1
inf = float("inf")
promedio = 0
contador = 0
mayor = 0
menor = inf
mayorNombre = ""
menorNombre = ""
notaPromedio = 0
while n != 0:
    nombre = input("ingrese el nombre de estudiante: ")
    if nombre == "FIN":
        break
    nota = float(input("ingrese la nota del estudiante: "))
 
    contador  = contador + 1
    notaPromedio = (notaPromedio + nota)
    promedio= notaPromedio/contador
    if nota > mayor:
        mayorNombre = nombre
        mayor = nota
    if nota < menor:
        menorNombre = nombre
        menor = nota
print(mayorNombre)
print(f"{mayor} fue la mayor nota ")
print(menorNombre)
print(f"{menor} es la menor nota ")
print(f"{promedio} fue el promedio general del grupo")