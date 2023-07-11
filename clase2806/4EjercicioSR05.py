valida = False

while valida == False:
    contra = input("ingrese la contreaseña: ")
    cant = len(contra)
    comparacion = contra.swapcase()
    
    if (cant >= 8):
        if comparacion != contra.upper() and comparacion != contra.lower():
            for i in range(1,cant):
                if contra[i].isdigit() == True:
                    valida = True
                if contra[i] == " ":
                    valida = False
                if contra[i] == "%" or contra[i] == "&":
                    valida == False
    if valida == True:
        print("contraseña valida")
    else:
        print("contraseña no valida")