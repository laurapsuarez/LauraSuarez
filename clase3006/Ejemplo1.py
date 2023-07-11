#  diseñar una funcion que calcule la media de tres numero 
# leidos por el teclado y poner un ejemplo de su
# aplicacio
def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Error  ingrese un numero entero valido.")
  

def media(n1,n2,n3):
    media = (n1+n2+n3)/3
    return media

a = leerInt("ingrese primer numero: ")
b = leerInt("ingrese segundo numero: ")
c = leerInt("ingrese el tercer numero: ")

prom = media(a,b,c)

print(f"la media de {a}, {b}, {c} es {prom:.3f}")