Nombre = input("ingrese el nombre del estudiante: ")
Calificacion = int(input("ingrese la calificacion del 0 a 100: "))
cualitativa = ""
if Calificacion <= 59 :
    cualitativa = "D"
elif Calificacion <= 79:
    cualitativa = "C"
elif Calificacion <= 89:
    cualitativa = "B"
else:
    cualitativa = "A"
print(f"Nombre del estudiante {Nombre} \n"
      f"Calificacion cuantitativa {Calificacion} \n"
      f"Calificacion cualitativa {cualitativa} \n")    