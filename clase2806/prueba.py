valida = False

while valida == False:
    contra = input("Ingrese una contraseña: ")
    longitud = len(contra)
    mayMin = contra.swapcase()
    numeros = 0
    espacios = 0
    especiales = 0
 
    #CONDICIÓN DE LONGITUD
    if(longitud >= 8):
        #CONDICIÓN MINUS Y MAYUS
        if mayMin != contra.upper() and mayMin != contra.lower():
            for i in range(1, longitud):
                #CONDICION NUMEROS
                if contra[i].isdigit() == True:
                    numeros += 1
                #CONDICION ESPACIOS
                if contra[i] == " ":
                    espacios += 1
                #CONDICIÓN CARACTERES ESPECIALES
                if contra[i] == "%" or contra[i] == "&" or contra[i] == "":
                    especiales += 1
            if numeros > 0:
                if espacios == 0:
                    if especiales > 0:
                        valida = True
                    else:
                        print("\nCONTRASEÑA NO VALIDA")
                        print("No contiene caracter especial")
                else:
                    print("\nCONTRASEÑA NO VALIDA")
                    print("Tiene Espacios")
            else:
                print("\nCONTRASEÑA NO VALIDA")
                print("NO Tiene Numeros")         
        else:
            print("CONTRASEÑA NO VALIDA")
            print("La contraseña no tiene al menos 1 Minuscula y 1 Mayuscula")
    else:
        print("CONTRASEÑA INVALIDA")
        print("La contraseña tiene menos de 8 digitos")

if valida == True:
    print("\nCONTRASEÑA VALIDA")
    print("Cumple con todas las condiciones")