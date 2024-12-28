import random

def multip():
    """Multiplica dos números aleatorios entre 1 y 3 e imprime el resultado."""
    a = random.randint(1, 3)
    b = random.randint(1, 3)
    resultado = a * b
    print(f"Resultado de la multiplicación: {a} * {b} = {resultado}")
    return resultado

def divi():
    """Divide dos números aleatorios entre 1 y 3 e imprime el resultado."""
    a = random.randint(1, 3)
    b = random.randint(1, 3)
    if b != 0:
        resultado = a / b
        print(f"Resultado de la división: {a} / {b} = {resultado:.2f}")
        return resultado
    else:
        print("No se puede dividir por 0.")