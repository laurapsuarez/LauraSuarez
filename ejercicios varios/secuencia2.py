Entrada = int(input("ingrese el numero inicial de segundos"))
horas = Entrada / 3600
minutos = (Entrada%3600)/60
segundos = (Entrada%60)
print("horas: %d, minutos: %d, segundos: %d"%(horas, minutos, segundos))