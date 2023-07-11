dicCat={1:25_000,2:30_000,3:40_000,4:45_000,5:60_000}

ttlHono = 0
dicDocentes = {}
while True:
    cedula = int(input("Ingrese cedula docente: "))
    nombre = input("Nombre del docente: ")
    categoria = int(input("Caregoria del docente: "))
    horas = int(input("Horas laboradas: "))
    dicDocentes[cedula] = {}
    dicDocentes[cedula]["Nombre"] = nombre
    dicDocentes[cedula]["Categoria"] = categoria
    dicDocentes[cedula]["Horas"] = horas
    
    opc = input("desea agregar otro docente? (si-no)")
    if opc.lower() == "no":
        break

print("\n\n *** INFORME ***")
print("-" * 30)
for k in dicDocentes.keys():
    h = dicDocentes[k]["Horas"] * dicCat[dicDocentes[k]["Categoria"]]
    print(dicDocentes[k]["Nombre"], f"-- ${h:,.0f}")
    ttlHono += h
print("-" * 30)
print(f"Total honorarios :${ttlHono:,}")