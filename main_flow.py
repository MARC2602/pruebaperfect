from prefect import task, flow
from archivo1 import buenosdias, suma
from archivo2 import multip

@task
def run_suma():
    """Ejecuta la función suma del archivo1 y retorna el resultado."""
    return suma()

@task
def run_multip():
    """Ejecuta la función multip del archivo2."""
    multip()

@task
def run_buenosdias_with_sum(suma_result):
    """
    Ejecuta la función buenosdias y añade el resultado de la suma al final del archivo.
    """
    buenosdias()
    
    # Añadir el resultado de la suma al final del archivo
    with open("buenosdias.txt", "a") as f:
        f.write(f"\nResultado de la suma: {suma_result}")

@flow
def main_pipeline():
    """Flujo principal que coordina las tareas."""
    # Ejecutar la suma y obtener su resultado
    suma_result = run_suma()

    # Ejecutar multiplicación en paralelo
    multip_result = run_multip.submit()

    # Esperar a que run_suma termine y obtener el resultado
    suma_value = suma_result

    # Condición: Solo ejecutar buenosdias si la suma es mayor o igual a 3
    if suma_value >= 5:
        run_buenosdias_with_sum(suma_value)

if __name__ == "__main__":
    main_pipeline()
