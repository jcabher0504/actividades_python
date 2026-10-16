matriculada = True
autorizacion_especial = False
edad = 17

puede_acceder = (matriculada and edad >= 18) or autorizacion_especial

print(f"Matriculada: {matriculada}, Edad: {edad}, Autorización: {autorizacion_especial}")
print(f"¿Puede acceder?: {puede_acceder}")

edad = 18
puede_acceder_caso2 = (matriculada and edad >= 18) or autorizacion_especial

print(f"¿Puede acceder caso 2?: {puede_acceder_caso2}")