
n = 1
while n > 0:
    n = int(input("ingrese un numero: "))
    primo = True
    for i in range (2,n):
        if n%i == 0:
            primo = False
    
    if n<0:
        break
          
    if primo == True:
        print(f"{n} es primo")
    else:
        print(f"{n} no es primo")