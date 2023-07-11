producto = input("ingrese el producto: ")
precio = int(input("ingrese el precio del producto: "))
cant = int(input("ingrese la cantidad: "))

total = precio * cant
bruto = total * 1.15

if bruto > 1000:
    bruto = bruto -(bruto/100*5)
    
print("*"*30)
print(f"{cant}  {producto}  {precio}")
print(f"precio total ${total:.0f} ")
print(f"precio bruto ${bruto:.0f}")