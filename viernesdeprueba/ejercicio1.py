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

while True: 
    companyName = leerString("Input a company name: ")
    comName = []
    for i in companyName:
       comName.append(i)
    
    dif = set(comName)

    if len(set(comName)) < 3:
        print("company name has at least 3 distintic characters ")
        continue
    
    name = {}

    for k in dif:
        t = companyName.count(k)
        print(k,t)
        name[k]=t

    
    newdic = name.copy()
    newdic = sorted(name.items())
    print(newdic)
    break
