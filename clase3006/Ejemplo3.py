# problema situacion liquidacion servicio de matricula

def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1 or n > 3:
                print("Error numero valido")
                input("digite cualquier tecla para continuar")
                continue
            return n
        except ValueError:
            print("Error  ingrese un numero entero valido.")
 
def leerString(msg):
    while True:
        try: 
            s = input(msg)
            if s == "" or s.strip() == " ":
                print("no ingrese un campo vacio")
                input("digite cualquier nombre para continuar")
                continue
            return s
        except Exception as e:
            print("error al ingresar un nombre",e.message)
 
def leerProgAcademi():
    print("*" * 40)
    print("1. Tecnico en sistemas.")
    print("2. Tecnico en Desarrollo de videojuegos.")
    print("3. Tecnico en Animacion Digital.")
    print("*" * 40)
    op = leerInt(" >> Opcion del 1 al 3?:")
    
    if op == 1:
        return 800_000
    elif op == 2:
        return 1_000_000
    else:
        return 1_200_000 
    

def leerIndiBeca():
    print("*" * 40)
    print("1. Beca por rendimiento academico.")
    print("2. Beca cultural-deportes.")
    print("3. Sin beca.") 
    print("*" * 40)
    bc = leerInt(">> Opcion del 1 al 3?: ")  
    
    if bc == 1:
        return 0.5
    if bc == 2:
        return 0.4
    else:
        return 1
    
def calMatricula(progAcademi,indiBeca):
    neto = progAcademi * indiBeca
    return neto
    
    
    
cod = leerInt("ingrese el codigo del estudiante: ")
nom = leerString("ingrese el nombre del estudiante: ")

progAcademi = leerProgAcademi()
indiBeca = leerIndiBeca()

valorNetoPagar = calMatricula(progAcademi,indiBeca)

print("\n", "*" * 40)
print("Estudiante: ",nom)
print(f"El valor neto a pagar es: ${valorNetoPagar:,.0f}")