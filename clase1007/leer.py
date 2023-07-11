import io

#abrir
fd = open("/home/spukN01-077/Documents/LauraSuarez/clase1007/texto.txt", "r", encoding="utf-8")


fd.seek(52)
#leer
# leer = fd.read()
leer2 = fd.readline(6)
leer3 = fd.readlines()
#cerrar
fd.close()

print(leer2.rstrip())
print(leer3)