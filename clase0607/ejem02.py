datosEstudiante = {}

def leerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Error!  ingrese un numero entero valido.")


def leerFloat(msg):
    while True:
        try:
            n = float(input(msg))
            if n > 5 or n < 0:
                print("ingrese un valor valido (0.0 - 5.0)")
                input("digite cualquier tecla para continuar")
                continue
            return n
        except ValueError:
            print("Error!  ingrese un numero entero valido.")

def leerString(msg):
    while True:
        try: 
            s = input(msg)
            if s == "" or s.strip() == " " :
                print("ingrese un campo valido")
                input("digite cualquier tecla para continuar")
                continue
            return s
        except Exception as e:
            print("error al ingresar un nombre",e.message)

def aprove(notaFinal):
    if notaFinal >= 3:
        return "aprobò"
    else:
        return "reprobò"
    
    
while True:
    codigo = leerInt("ingrese codigo estudiante: ")
    
        
    if codigo == 999:
        break    
    
    
    nombre = leerString("ingrese nombre estudiante: ")
    nota1 = leerFloat("ingrese nota 1: ")
    nota2 = leerFloat("ingrese nota 2: ")
    nota3 = leerFloat("ingrese nota 3: ")


    
    datosEstudiante[codigo] = {}
    datosEstudiante[codigo]["nombre"] = nombre
    datosEstudiante[codigo]["nota1"] = nota1
    datosEstudiante[codigo]["nota2"] = nota2
    datosEstudiante[codigo]["nota3"] = nota3
    
    notaEstu1 = datosEstudiante[codigo]["nota1"] * 0.3
    notaEstu2 = datosEstudiante[codigo]["nota2"] * 0.3
    notaEstu3 = datosEstudiante[codigo]["nota3"] * 0.4
    
    notaFinal = notaEstu1 + notaEstu2 + notaEstu3
    print(aprove(notaFinal)) 
    print(f"Nota final fue: {notaFinal}")

                                                                                                                                                                                                                                          
