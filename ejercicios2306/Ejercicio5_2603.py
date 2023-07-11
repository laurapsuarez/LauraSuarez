Dia = int(input("ingrese el dia: "))
Mes = int(input("ingrese el mes: "))
Year = int(input("ingrese el año: "))

print(f"Fecha inicial: {Dia}-{Mes}-{Year}") 


if Mes == 12 and Dia == 31:
    Year = Year + 1
    Mes = 1
    Dia = 1
    print(f"Nueva Fecha: {Dia}-{Mes}-{Year}")
elif Mes == 12 and Dia != 31:
    Dia = Dia +1
    print(f"3Nueva Fecha: {Dia}-{Mes}-{Year}")
    
if (Mes == 1 or Mes == 3 or Mes == 5 or Mes == 7 or Mes == 8 or Mes == 10) and Dia == 31:
    Mes = Mes + 1
    Dia = 1
    print(f"Nueva Fecha: {Dia}-{Mes}-{Year}")
else:
    Dia = Dia + 1
    print(f"1Nueva Fecha: {Dia}-{Mes}-{Year}")
    
if (Mes == 4 or Mes == 6 or Mes == 9 or Mes == 11) and Dia == 30:
    Mes = Mes + 1
    Dia = 1
    print(f"Nueva Fecha: {Dia}-{Mes}-{Year}")
       
if Mes == 2:
    if Year%100 == 0 and Year%400 !=0:
        if Dia == 28:
            Dia = 1
            Mes = 3
            print(f"Nueva Fecha: {Dia}-{Mes}-{Year}")
    elif Year%4 == 0:
        if Dia == 29:
            Dia = 1
            Mes = 3
            print(f"Nueva Fecha: {Dia}-{Mes}-{Year}")