DINERO_CINE = 10
TIEMPO_CINE = 2
DINERO_COMER = 30
TIEMPO_COMER = 2
DINERO_MUSEO = 5
TIEMPO_MUSEO = 1
DINERO_DEPORTE = 0
TIEMPO_DEPORTE = 1
DINERO_CASA = 0
TIEMPO_CASA = 3

dinero = int(input("Dinero disponible: "))
tiempo = int(input("Tiempo disponible: "))


def actividad():
    print("¿Qué quieres hacer?")
    print("1. ir al cine (10€ / 2 horas)")
    print("2. salir a comer (30€ / 2 horas)")
    print("3. visitar un museo (5€ / 1 horas)")
    print("4. hacer deporte (0€ / 1 horas)")
    print("5. quedarse en casa (0€ / 3 horas)")    



while dinero > 0 and tiempo > 0 or tiempo > 0:
    actividad()
    hacer = int(input("Elección: "))
    
    match opcion:
        case 