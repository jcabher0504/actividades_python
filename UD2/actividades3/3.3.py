precio = 170
pagado = 0

while pagado < precio:
    moneda = int(input("Introduce una moneda (10, 20, 50 o 100): "))
    
    if moneda == 10 or moneda == 20 or moneda == 50 or moneda == 100:
        pagado += moneda
        if pagado < precio:
            print(f"Llevas {pagado} céntimos. Faltan {precio - pagado} céntimos.")
    else:
        print("Moneda no aceptada.")

cambio = pagado - precio
print("Producto entregado.")
print(f"Cambio a devolver: {cambio} céntimos ({cambio / 100} euros).")