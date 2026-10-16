total_segundos = 7384

horas = total_segundos // 3600
minutos_restantes = (total_segundos % 3600) // 60
segundos_restantes = total_segundos % 60


print(f"{total_segundos} segundos equivalen a:")
print(f"{horas} horas {minutos_restantes} minutos y {segundos_restantes} segundos")
