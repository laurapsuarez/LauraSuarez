def msgError(msg):
    print(" ERROR ", msg)

def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            msgError("ingrese un numero entero valido")

def leerString(msg):
    while True:
        s = input(msg)
        st = s.strip()
        if s == "" or s.strip() == " ":
            msgError("no ingrese un campo vacio")
            continue
        return st
    
def leerHoras(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1 or n > 160:
                print("Ingrese un valor valido entre 1-160")
                input("Digite cualquier nombre para continuar")
                continue
            return n
        except ValueError:
            msgError("ingrese un numero entero valido")    

def leerValor(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 8_000 or n > 150_000:
                print("Ingrese un valor valido entre 8.000 - 150.000")
                input("Digite cualquier nombre para continuar")
                continue
            return n
        except ValueError:
            msgError("ingrese un numero entero valido")      

emple = {}

def agreEmple():
    print("\n********")
    print("1. Agregar empleado")
    print("********\n")
    id = leerInt("ingrese el ide del empleado: ")
    nom = leerString("ingrese el nombre del empleado: ")
    horas = leerHoras("ingrese las horas trabajadas por el empleado: ")
    valor = leerValor("ingrese el valor de las horas trabajadas por el trabajador: $")
    
    emple[id] = {}
    emple[id]["nombre"] = nom
    emple[id]["horas"] = horas
    emple[id]["valor"] = valor
    
    print(emple)
    
    input("presione cualquier letra para volver al menu")

def modEmple():
    try:
        print("\n********")
        print("2. Modificar Empleado")
        print("********\n") 
        id = leerInt("ingrese el ide del empleado al que desea modificar los datos: ")  
        print("DATOS ACTUALES")
        print("Nombre: ",emple[id]["nombre"])
        moNom = leerString("desea modificar el nombre? (si-no)")
        if moNom == "si":
            nom = leerString("ingrese el nuevo nombre del empleado: ")
            emple[id]["nombre"] = nom
        print("Horas trabajadas: ",emple[id]["horas"])
        moHoras =  leerString("desea modificar el horas? (si-no)") 
        if moHoras == "si":
            horas = leerHoras("ingrese las nuevas horas trabajadas por el empleado: ")
 
            emple[id]["horas"] = horas
        print("valor de la hora: $",emple[id]["valor"])
        moValor = leerString("desea modificar el valor de las horas? (si-no)") 
        if moValor == "si":
            valor = leerValor("ingrese el nuevo valor de las horas trabajadas por el trabajador: ")
            emple[id]["valor"] = valor
            
        print(emple)
        input("presione cualquier letra para volver al menu")           

    except ValueError:
        msgError("id no encontrado")

def busEmple():
    try:
        print("\n********")
        print("3. Buscar empleado")
        print("********\n") 
        id = leerInt("ingrese el ide del empleado del que desea buscar los datos: ")  
        print("DATOS ACTUALES")
        print("Id: ",emple[id])
        print("Nombre: ",emple[id]["nombre"])
        print("Horas trabajadas: ",emple[id]["horas"])
        print("valor de la hora: $",emple[id]["valor"])
        input("presione cualquier letra para volver al menu")   
    except ValueError:
        msgError("id no encontrado")   
    
def eliEmple():
    try:
        print("\n********")
        print("4. Eliminar Empleado")
        print("********\n") 
        id = leerInt("ingrese el ide del empleado del que desea eliminar los datos: ")  
        emple[id] = {}
        emple[id]["nombre"] = None
        emple[id]["horas"] = None
        emple[id]["valor"] = None

        print("Los datos han sido eliminados satisfactoriamente ")
        input("presione cualquier letra para volver al menu") 
    except ValueError:
        msgError("id no encontrado")  

def listEmple():
    print("\n********")
    print("5. Listar empleados")
    print("********\n") 
    totalEmple = len(emple.keys())
    for i in range(0,totalEmple,5):
        print("-"*30)
        for j in range (i,min(i+5,totalEmple)):
            for k in emple.keys():
                print("Id: ",k )
                print("Nombre: ",emple[k]["nombre"] )
                print("Horas trabajadas: ",emple[k]["horas"])
                print("Valor de la hora: $",emple[k]["valor"])
                print("-" * 30)   

        if j < totalEmple -1:
            opcion = leerString("desea ver mas empleados? (si-no)") 
            if opcion != "si":
                break
    input("presione cualquier letra para volver al menu")               

def nominaEmple():
    print("\n********")
    print("6. Lista nomina de un empleado")
    print("********\n")
    try:
        id = leerInt("ingrese el ide del empleado del que desea saber la nomina: ")  
        print("DATOS ACTUALES")
        print("Id: ",emple[id])
        print("Nombre: ",emple[id]["nombre"])
        print("Horas trabajadas: ",emple[id]["horas"])
        print("valor de la hora: $",emple[id]["valor"])
        salBruto = emple[id]["horas"]*emple[id]["valor"]
        print(f"Salario bruto: ${salBruto:,}",)
        auxTrans = 0
        if salBruto < 1_300_606 :
            auxTrans = 140_606
        print("Auxilio de transporte: $",auxTrans)
        descuentos = salBruto*0.04
        print(f"Eps: {descuentos:,}")
        print(f"Pension: {descuentos:,}")
        salNeto = salBruto + auxTrans - (descuentos*2)
        print(f"salario neto: ${salNeto:,}")


        input("presione cualquier letra para volver al menu")   
    except ValueError:
        msgError("id no encontrado")        

def listNomEmpl():
    print("\n********")
    print("7. Listar nomina de todos los empleados")
    print("********\n")   
    totalEmple = len(emple.keys())
    for i in range(0,totalEmple,5):
        print("-"*30)
        for j in range (i,min(i+5,totalEmple)):
            for k in emple.keys():
                print("Id: ", k)
                print("Nombre: ",emple[k]["nombre"])
                print("Horas trabajadas: ",emple[k]["horas"])
                print("Valor de la hora: $",emple[k]["valor"])
                salBruto = emple[k]["horas"]*emple[k]["valor"]
                print("Salario bruto: $",salBruto)
                auxTrans = 0
                if salBruto < 1_300_606 :
                    auxTrans = 140_606
                print("Auxilio de transporte: $",auxTrans)
                descuentos = salBruto*0.04
                print(f"Eps: ${descuentos:,}")
                print(f"Pension: ${descuentos:,}")
                salNeto = salBruto + auxTrans - (descuentos*2)
                print(f"salario neto: ${salNeto:,}")            
                print("-" * 30)   
        if j < totalEmple -1:
            opcion = leerString("desea ver mas empleados? (si-no)") 
            if opcion != "si":
                break
    input("presione cualquier letra para volver al menu")        

def menu():
    while True:
        print("\n********")
        print(" MENU ")
        print("********\n")
        print("1. Agregar empleado")
        print("2. Modificar Empleado")   
        print("3. Buscar empleado")
        print("4. Eliminar Empleado")
        print("5. Listar empleados")
        print("6. Lista nomina de un empleado")
        print("7. Listar nomina de todos los empleados")
        print("8. Salir")

        op = leerInt("\n >> Escoja una opcion  (1-8)? ")
        if op < 1 or op > 8:
            msgError("Opcion no valida")
            continue
        return op
    
while True:
    opcion = menu()

    if opcion == 1:
        agreEmple()
    elif opcion == 2:
        modEmple()
    elif opcion == 3:
        busEmple()
    elif opcion == 4:
        eliEmple()
    elif opcion == 5:
        listEmple()
    elif opcion == 6:
        nominaEmple()
    elif opcion == 7:
        listNomEmpl()
    elif opcion == 8:
        print("\n *** GRACIAS POR USAR ***")
        break