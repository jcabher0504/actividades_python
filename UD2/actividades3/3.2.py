numero = int(input("Introduce un número entero mayor que 1: "))
es_primo = True
divisor = 2

while divisor < numero and es_primo:
    if numero % divisor == 0:
        es_primo = False
    divisor += 1

if es_primo:
    print(f"El {numero} es primo.")
else:
    print(f"El {numero} no es primo.")