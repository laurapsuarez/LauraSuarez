import math
p = int(input("ingrese el valor p: "))
a = int(input("ingrese el valor a: "))
c = int(input("ingrese el valor c: "))
b = int(input("ingrese el valor b: "))

if p>a and p>b and p>c:
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"para un triangulo de lados {p},{a},{c},{b} el area es {area:.2f}")
else:
    print("datos no validos")