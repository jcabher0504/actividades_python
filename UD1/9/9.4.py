plazas = 12
plazas -= 3
plazas += 1

print(f"Número final de plazas disponibles: {plazas}")

estado = "Hay plazas" if plazas > 0 else "Completo"
print(f"Estado del aula: {estado}") 
