edad = int(input("Introduce tu edad: "))
    
if edad < 0:
    print("Error: la edad no puede ser negativa.")
else:
    dia = input("Introduce el día de la semana: ").strip().lower()
    sesion_3d = input("¿La sesión es en 3D? (sí/no): ").strip().lower()
    
    precio = 0
    
    if edad < 12:
        precio = 5
        print("Entrada infantil: 5 euros")
    elif edad >= 65:
        precio = 6
        print("Entrada jubilado: 6 euros")
    else:
        precio = 8
        print("Entrada general: 8 euros")
        
    if dia == "miércoles" or dia == "miercoles":
        precio = precio - 1
        print("Descuento miércoles: -1 euro")
        
    if sesion_3d == "sí" or sesion_3d == "si":
        precio = precio + 2
        print("Suplemento 3D: +2 euros")
        
    print("PRECIO FINAL:", precio, "euros")