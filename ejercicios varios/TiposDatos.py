Nombre = input("ingrese el nombre del empleado")
Salario = int(input("ingrese salario"))

SubTrans = 0

if Salario <= 1200000:
    SubTrans = 120000
print("\n","-"*30)
print(f"El nombre del empleado es {Nombre} \n"
      f"el salario es  {Salario:,.0f} \n"
      f"el subsidio de transporte es {SubTrans:,.0f}")

