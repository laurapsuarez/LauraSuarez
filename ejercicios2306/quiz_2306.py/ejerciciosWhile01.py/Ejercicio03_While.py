inf = float("inf")
n = 1
mayor = 0
menor = inf
while n>0:
    n = int(input("ingrese un numero positivo: ")) 
    if n<0:
        break

    if n>mayor:
        mayor = n
    if n<menor:
        menor = n


print(f"{mayor} fue el numero mayor ")
print(f"{menor} es el numero menor ")