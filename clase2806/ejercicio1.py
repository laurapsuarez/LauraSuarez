
vocal = False

while True:
    
    
    while True :
        vocales = 0
        fra = input("ingrese una frase: ")
        if fra == "" or fra.strip() == "":
            print("ingrese una frase valida")
            continue
        break
    
    while True:
        cand = len(fra)
   
        if "a" in fra:
            vocales = vocales + fra.count("a")
        if "e" in fra:
            vocales = vocales + fra.count("e")
        if "i" in fra:
            vocales = vocales + fra.count("i")
        if "o" in fra:
            vocales = vocales + fra.count("o")
        if "u" in fra:
            vocales = vocales + fra.count("u")
        
        
        
        print(vocales)
        break

    if fra.upper() == "Q":
        break