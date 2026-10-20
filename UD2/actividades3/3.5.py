import random

titular = "Jose Caballero"
cuenta_activa = True
saldo = random.randint(0, 1000)
operacion = ""


while operacion != "salir": 
    
    operacion = input("Elige una operación: ingresar, retirar, consultar, cerrar cuenta, abrir cuenta o salir:  ").strip().lower()

    match operacion:
        case "ingresar":
            if cuenta_activa:
                cantidad = float(input("Cantidad a ingresar: "))
                saldo += cantidad
                print(f"Ingreso realizado. Saldo actual: {saldo} €")
            else:
                print("Operación rechazada: La cuenta está cerrada.")
                
        case "retirar":
            if cuenta_activa:
                cantidad = float(input("Cantidad a retirar: "))
                if cantidad <= saldo:
                    saldo -= cantidad
                    print(f"Retirada realizada. Saldo actual: {saldo} €")
                else:
                    print(f"Operación rechazada: Saldo insuficiente. Saldo actual: {saldo} €")
            else:
                print("Operación rechazada: La cuenta está cerrada.")
                
        case "consultar":
            estado = "Activa" if cuenta_activa else "Cerrada"
            print(f"Titular: {titular}")
            print(f"Saldo actual: {saldo} €")
            print(f"Estado de la cuenta: {estado}")
            
        case "cerrar cuenta":
            if cuenta_activa:
                if saldo == 0:
                    cuenta_activa = False
                    print("La cuenta se ha cerrado correctamente.")
                else:
                    print("Operación rechazada: Para cerrar la cuenta el saldo debe ser 0 €.")
            else:
                print("Operación rechazada: La cuenta ya está cerrada.")
                
        case "abrir cuenta":
            if not cuenta_activa:
                cuenta_activa = True
                saldo = 0
                print("La cuenta se ha abierto correctamente. Saldo inicial: 0 €")
            else:
                print("Operación rechazada: La cuenta ya está activa.")
                
        case "salir":
            estado = "Activa" if cuenta_activa else "Cerrada"
            print(f"Saliendo... Estado final -> Titular: {titular} | Saldo: {saldo} € | Estado: {estado}")
            
        case _:
            print("Operación no válida, por favor elige una opción del menú.")