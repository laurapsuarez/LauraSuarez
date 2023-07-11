Hora = int(input("ingrese el valor de la hora: "))
Minuto = int(input("ingrese el valor de los minutos: "))
Segundos = int(input("ingrese el valor de los segundos: "))
Horario = input("ingrese AM o PM segun sea el caso: ")

if Horario == "AM" or Horario == "am":
    if Hora == 12:
        Hora = 0
    print(f"{Hora:02d}:{Minuto:02d}:{Segundos:02d}")
elif Horario == "PM" or Horario == "pm":
    if Hora != 12:
        Hora = Hora + 12
    print(f"{Hora:02d}:{Minuto:02d}:{Segundos:02d}")
else:
    print("ingrese un horario valido")