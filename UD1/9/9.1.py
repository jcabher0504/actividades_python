precio = 24.50
unidades = 3
porcentaje_descuento = 10.0  # 10% de descuento
umbral_envio = 50.0

subtotal = precio * unidades
descuento = subtotal * (porcentaje_descuento / 100)
base_imponible = subtotal - descuento
iva = base_imponible * 0.21  # IVA general del 21%
total = base_imponible + iva

print(f"Subtotal:    {subtotal:.2f} €")
print(f"Descuento:   {descuento:.2f} €")
print(f"IVA (21%):   {iva:.2f} €")
print(f"Total:       {total:.2f} €")

supera_envio = total >= umbral_envio
print(f"¿Supera el umbral de envío gratuito?: {supera_envio}")