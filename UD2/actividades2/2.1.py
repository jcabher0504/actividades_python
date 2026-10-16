import random

operacion = input("¿Qué operació quieres realizar: ingresar, retirar, abrir cuenta, cerrar cuenta o consultar?")
operacion_limpia = operacion.lower().strip()
titular = "Jose Caballero"
saldo = random.randint(0,1000)
estado = True


match operacion_limpia:
    case "ingresar":
        cantidad = int(input("Dinero a ingresar: "))
        if cantidad > 0:
            saldo += cantidad
        else:
            print("Cantidad no válida")
    case "retirar":
        cantidad = int(input("Dinero a retirar: "))
        if cantidad > 0 and saldo >= cantidad:
            saldo -= cantidad
        else:
            print("Cantidad no válida")
    case "abrir":
        if not estado:
            estado = True
        else:
            print("Cuenta ya activada")
    case "cerrar":
        if estado and saldo == 0:
            estado = False
            print("Cuenta cerrada")
        else:
            print("La cuenta ya está cerrada")
    case "consultar":
        print(titular, "tu saldo es ",saldo)
    case _:
        print("Operación no válida") 