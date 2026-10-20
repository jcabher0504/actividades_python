aforo_maximo = 8
ocupado = 0
accion = ""

while accion != "fin":
    accion = input("Escribe una acción (entra, sale, fin): ")
    
    match accion:
        case "entra":
            if ocupado < aforo_maximo:
                ocupado += 1
                print(f"Aforo actual: {ocupado}")
            else:
                print("La sala está llena, no puede entrar nadie más.")
                
        case "sale":
            if ocupado > 0:
                ocupado -= 1
                print(f"Aforo actual: {ocupado}")
            else:
                print("La sala está vacía, no hay nadie para salir.")
                
        case "fin":
            print(f"Control terminado. Quedan {ocupado} personas en la sala.")
            
        case _:
            print("Acción no válida.")