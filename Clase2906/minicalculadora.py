# programa general 
def msgError(msg):
    print(" ERROR ", msg)

def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Error  ingrese un numero entero valido.")

def menu():
    while True:
        print("\n********")
        print(" MENU ")
        print("********\n")
        print("1. sumar")
        print("2. restar")   
        print("3. multiplicar")
        print("4. division")
        print("5. potencia")    
        print("6. factorial")
        print("7. salir")
        op = leerInt("\n opcion (1 a 7)? ")
        if op < 1 or op > 7:
            msgError("Opcion no valida")
            continue
        return op


def sumar():
    print("\n" * 3,"*** 1. SUMAR ***")
    n1 = leerInt("ingrese un numero: ")
    n2 = leerInt("ingrese otra numero: ")
    print("el resultado de la suma es: ",n1 + n2)
    input("presione cualquier tecla para volver al menu")

def restar():
    print("\n" * 3,"*** 2. RESTAR ***")
    n1 = leerInt("ingrese un numero: ")
    n2 = leerInt("ingrese otra numero: ")
    print("el resultado de la resta es: ",n1 - n2)
    input("presione cualquier tecla para volver al menu")  

def multiplicar():
    print("\n" * 3,"*** 3. MULTIPLICAR ***")
    n1 = leerInt("ingrese un numero: ")
    n2 = leerInt("ingrese otra numero: ")
    print("el resultado de la multiplicacion es: ",n1 * n2)
    input("presione cualquier tecla para volver al menu")

def dividir():
    print("\n" * 3,"*** 4. DIVIDIR ***")
    n1 = leerInt("ingrese un numero: ")
    while True:
        n2 = leerInt("ingresa un numero: ")
        if n2 == 0:
            print("ingresa un numero diferente de 0")
            continue
        break  
    print("el resultado de la division es:",round(n1/n2,2))
    input("presione cualquier tecla para volver al menu")   
    
        

def potencia():
    print("\n" * 3,"*** 5. POTENCIA ***")
    n1 = leerInt("ingrese un numero: ")
    n2 = leerInt("ingrese otra numero: ")
    print("el resultado de la potencia es: ",n1 ** n2)
    input("presione cualquier tecla para volver al menu")
    

def factorial():
    print("\n" * 3,"*** 6. FACTORIAL ***")
    n1 = leerInt("ingrese un numero: ")
    f = 1
    for i in range(1,n1+1):
        f *= i
    print("el resultado de la suma es: ",i)
    input("presione cualquier tecla para volver al menu")    


while True:
    opcion = menu()
    
    if opcion == 1:
        sumar()
    elif opcion == 2:
        restar()
    elif opcion == 3:
        multiplicar()
    elif opcion == 4:
        dividir()
    elif opcion == 5:
        potencia()
    elif opcion ==6:
        factorial()
    elif opcion == 7:
        print("\n ** gracias por usar **")
        break
    else:
        msgError("Opcion invalida")