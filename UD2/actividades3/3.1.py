codigo_correctro = "4826"
intentos = 3
acceso_concedido = False

while intentos > 0 and not acceso_concedido:
    codigo_usuario = input("Introduce el código de acceso: ")

    if codigo_usuario == codigo_correctro:
        acceso_concedido = True
        print("Acceso autorizado.")
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Código incorrecto. Te quedan {intentos} intentos.")
        else:
            print("Acceso denegado")