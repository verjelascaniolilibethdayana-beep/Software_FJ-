"""
Proyecto: Software FJ
Archivo: simulacion_operaciones.py

Descripción:
Simulación básica de operaciones para probar Cliente y
AlquilerEquipo con casos válidos e inválidos.

Nota:
Este archivo está pensado como avance del integrante que
desarrolla alquiler_equipo.py. Cuando el grupo complete el
resto de clases del sistema, esta simulación podrá ampliarse
con reservas y más servicios.
"""

from cliente import Cliente
from alquiler_equipo import AlquilerEquipo


def ejecutar_simulacion():
    # Lista donde guardamos resultados de las operaciones.
    resultados = []

    # Operación 1: crear un cliente válido.
    try:
        cliente1 = Cliente("C001", "Juan David Moreno", "juan@email.com", "3123456789")
        resultados.append("Cliente válido creado correctamente.")
        resultados.append(cliente1.mostrar_informacion())
    except Exception as error:
        resultados.append(f"Error creando cliente válido: {error}")

    # Operación 2: intentar crear un cliente inválido.
    try:
        Cliente("C002", "", "correo_invalido", "123")
    except Exception as error:
        resultados.append(f"Cliente inválido detectado: {error}")

    # Operación 3: crear un alquiler válido.
    try:
        alquiler1 = AlquilerEquipo("S001", "Alquiler de equipos", 50000,
                                   "Portátil Lenovo", 3, True)
        resultados.append("Alquiler válido creado correctamente.")
        resultados.append(alquiler1.mostrar_informacion())
    except Exception as error:
        resultados.append(f"Error creando alquiler válido: {error}")

    # Operación 4: verificar disponibilidad.
    try:
        resultados.append(
            f"¿Equipo disponible? {alquiler1.verificar_disponibilidad()}"
        )
    except Exception as error:
        resultados.append(f"Error verificando disponibilidad: {error}")

    # Operación 5: calcular costo del alquiler.
    try:
        resultados.append(f"Costo calculado: ${alquiler1.calcular_costo():,.2f}")
    except Exception as error:
        resultados.append(f"Error calculando costo: {error}")

    # Operación 6: intentar crear un alquiler con días negativos.
    try:
        AlquilerEquipo("S002", "Alquiler de equipos", 40000,
                       "Monitor", -2, True)
    except Exception as error:
        resultados.append(f"Alquiler inválido detectado: {error}")

    # Operación 7: intentar crear un alquiler con nombre vacío.
    try:
        AlquilerEquipo("S003", "Alquiler de equipos", 40000,
                       "", 2, True)
    except Exception as error:
        resultados.append(f"Nombre de equipo inválido detectado: {error}")

    # Operación 8: crear un alquiler no disponible.
    try:
        alquiler2 = AlquilerEquipo("S004", "Alquiler de equipos", 60000,
                                   "Proyector Epson", 2, False)
        resultados.append("Alquiler no disponible creado correctamente.")
        resultados.append(alquiler2.mostrar_informacion())
    except Exception as error:
        resultados.append(f"Error creando alquiler no disponible: {error}")

    # Operación 9: modificar la disponibilidad del segundo equipo.
    try:
        alquiler2.disponible = True
        resultados.append(
            f"Disponibilidad actualizada: {alquiler2.verificar_disponibilidad()}"
        )
    except Exception as error:
        resultados.append(f"Error actualizando disponibilidad: {error}")

    # Operación 10: mostrar resumen final.
    resultados.append("Simulación finalizada correctamente.")

    for mensaje in resultados:
        print(mensaje)


if __name__ == "__main__":
    ejecutar_simulacion()
