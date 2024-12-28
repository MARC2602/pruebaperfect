import random

def buenosdias():
    """Crea un archivo de texto con 'Buenos días' repetido 10 veces."""
    with open("buenosdias.txt", "w") as f:
        for _ in range(10):
            f.write("Buenos días\n")
    print("Archivo 'buenosdias.txt' creado con 10 líneas de 'Buenos días'.")

def suma():
    """Suma dos números aleatorios entre 1 y 3 e imprime el resultado."""
    a = random.randint(1, 3)
    b = random.randint(1, 3)
    resultado = a + b
    print(f"Resultado de la suma: {a} + {b} = {resultado}")
    return resultado