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

empleId =[]
empleNombre = []
empleHoras = []
empleValor = []

def agreEmple():
    print("\n********")
    print("1. Agregar empleado")
    print("********\n")
    id = leerInt("ingrese el ide del empleado: ")
    empleId.append(id)
    nom = leerString("ingrese el nombre del empleado: ")
    empleNombre.append(nom)
    horas = leerHoras("ingrese las horas trabajadas por el empleado: ")
    empleHoras.append(horas)
    valor = leerValor("ingrese el valor de las horas trabajadas por el trabajador: $")
    empleValor.append(valor)
    input("presione cualquier letra para volver al menu")

def modEmple():
    try:
        print("\n********")
        print("2. Modificar Empleado")
        print("********\n") 
        id = leerInt("ingrese el ide del empleado al que desea modificar los datos: ")  
        index = empleId.index(id)
        print("DATOS ACTUALES")
        print("Nombre: ",empleNombre[index])
        moNom = leerString("desea modificar el nombre? (si-no)")
        if moNom == "si":
            nom = leerString("ingrese el nuevo nombre del empleado: ")
            empleNombre.pop(index)
            empleNombre.insert(index,nom)
        print("Horas trabajadas: ",empleHoras[index])
        moHoras =  leerString("desea modificar el horas? (si-no)") 
        if moHoras == "si":
            horas = leerHoras("ingrese las nuevas horas trabajadas por el empleado: ")
            empleHoras.pop(index)
            empleHoras.insert(index,horas)
        print("valor de la hora: $",empleValor[index])
        moValor = leerString("desea modificar el valor de las horas? (si-no)") 
        if moValor == "si":
            valor = leerValor("ingrese el nuevo valor de las horas trabajadas por el trabajador: ")
            empleValor.pop(index)
            empleValor.insert(index,valor)
        input("presione cualquier letra para volver al menu")           

    except ValueError:
        msgError("id no encontrado")



def busEmple():
    try:
        print("\n********")
        print("3. Buscar empleado")
        print("********\n") 
        id = leerInt("ingrese el ide del empleado del que desea buscar los datos: ")  
        index = empleId.index(id)
        print("DATOS ACTUALES")
        print("Id: ",empleId[index])
        print("Nombre: ",empleNombre[index])
        print("Horas trabajadas: ",empleHoras[index])
        print("valor de la hora: $",empleValor[index])
        input("presione cualquier letra para volver al menu")   
    except ValueError:
        msgError("id no encontrado")   
    

def eliEmple():
    try:
        print("\n********")
        print("4. Eliminar Empleado")
        print("********\n") 
        id = leerInt("ingrese el ide del empleado del que desea eliminar los datos: ")  
        index = empleId.index(id)  
        empleNombre.pop(index)  
        empleHoras.pop(index)
        empleValor.pop(index)
        print("Los datos han sido eliminados satisfactoriamente ")
        input("presione cualquier letra para volver al menu") 
    except ValueError:
        msgError("id no encontrado")  

def listEmple():
    print("\n********")
    print("5. Listar empleados")
    print("********\n")  
    totalEmple = len(empleId)
    for i in range(0,totalEmple,5):
        print("-"*30)
        for j in range (i,min(i+5,totalEmple)):
            print(j)
            print("Id: ", empleId[j])
            print("Nombre: ", empleNombre[j])
            print("Horas trabajadas: ", empleHoras[j])
            print("Valor de la hora: $", empleValor[j])
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
        index = empleId.index(id)
        print("DATOS ACTUALES")
        print("Id: ",empleId[index])
        print("Nombre: ",empleNombre[index])
        print("Horas trabajadas: ",empleHoras[index])
        print("valor de la hora: $",empleValor[index])
        salBruto = empleHoras[index]*empleValor[index]
        print("Salario bruto: $",salBruto)
        auxTrans = 0
        if salBruto < 1_300_606 :
            auxTrans = 140_606
        print("Auxilio de transporte: $",auxTrans)
        descuentos = auxTrans*0.04
        print(f"Eps: {descuentos:.0}")
        print(f"Pension: {descuentos:.0}")
        salNeto = salBruto + auxTrans - (descuentos*2)
        print(f"salario neto: ${salNeto:.0}")


        input("presione cualquier letra para volver al menu")   
    except ValueError:
        msgError("id no encontrado")        

def listNomEmpl():
    print("\n********")
    print("7. Listar nomina de todos los empleados")
    print("********\n")   
    totalEmple = len(empleId)
    for i in range(0,totalEmple,5):
        print("-"*30)
        for j in range (i,min(i+5,totalEmple)):
            print("Id: ", empleId[j])
            print("Nombre: ", empleNombre[j])
            print("Horas trabajadas: ", empleHoras[j])
            print("Valor de la hora: $", empleValor[j])
            salBruto = empleHoras[j]*empleValor[j]
            print("Salario bruto: $",salBruto)
            auxTrans = 0
            if salBruto < 1_300_606 :
                auxTrans = 140_606
            print("Auxilio de transporte: $",auxTrans)
            descuentos = auxTrans*0.04
            print(f"Eps: ${descuentos:.0}")
            print(f"Pension: ${descuentos:.0}")
            salNeto = salBruto + auxTrans - (descuentos*2)
            print(f"salario neto: ${descuentos:.0}")            
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