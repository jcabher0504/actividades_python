palabra = input("Introduce una palabra: ").strip().lower()
letras = {}

for letra in palabra:
    if letra not in letras:
        letras[letra] = palabra.count(letra)




print(letras)
