# funcion que suma dos numeros

def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Error  ingrese un numero entero valido.")
            

def suma(num1, num2):
    s = num1 + num2
    return s

a = leerInt("ingrese un numero ")
b = leerInt("ingrese otro numero ")
print("El resultado es", suma(a,b))