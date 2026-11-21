"""Simulaciones integradas de clientes, alquileres, salas y reservas.

Ejecutar desde la raíz de Software FJ con:
    python simulacion_operaciones.py
"""

from cliente import Cliente
from alquiler_equipo import AlquilerEquipo
from reserva import Reserva
from excepciones import ReservaInvalidaError
from servicio import ReservaSala
from configuracion_logs import configurar_logging, registrar_error, registrar_evento


def ejecutar_simulacion(mostrar=True):
    """Ejecuta operaciones válidas e inválidas y devuelve sus resultados.

    Los errores esperados de validación se registran sin detener la simulación.
    Los objetos creados se comprueban antes de acceder a sus métodos.
    """
    configurar_logging()
    resultados = []
    cliente1 = None
    alquiler1 = None
    alquiler2 = None
    sala1 = None
    reserva1 = None

    def exitoso(mensaje):
        resultados.append(mensaje)
        registrar_evento("Simulación: %s", mensaje)

    def fallo(operacion, error):
        mensaje = f"{operacion}: {error}"
        resultados.append(mensaje)
        registrar_error(operacion, error)

    # 1. Cliente válido y cliente con datos incorrectos.
    try:
        cliente1 = Cliente("C001", "Juan David Moreno", "juan@email.com", "3123456789")
        exitoso("Cliente válido creado correctamente.")
        resultados.append(cliente1.mostrar_informacion())
    except Exception as error:
        fallo("Error creando cliente válido", error)

    try:
        Cliente("C002", "", "correo_invalido", "123")
        fallo("Validación de cliente inválido", AssertionError("Se aceptaron datos inválidos."))
    except ValueError as error:
        exitoso(f"Cliente inválido detectado: {error}")
    except Exception as error:
        fallo("Error inesperado al validar cliente", error)

    # 2. Alquiler válido y sus operaciones.
    try:
        alquiler1 = AlquilerEquipo("S001", "Alquiler de equipos", 50000,
                                   "Portátil Lenovo", 3, True)
        exitoso("Alquiler válido creado correctamente.")
        resultados.append(alquiler1.mostrar_informacion())
    except Exception as error:
        fallo("Error creando alquiler válido", error)

    if alquiler1 is not None:
        try:
            exitoso(f"¿Equipo disponible? {alquiler1.verificar_disponibilidad()}")
            exitoso(f"Costo calculado: ${alquiler1.calcular_costo():,.2f}")
        except Exception as error:
            fallo("Error consultando alquiler válido", error)
    else:
        exitoso("No se consultó el alquiler porque no pudo crearse.")

    for descripcion, datos in (
        ("Días negativos", ("S002", "Alquiler de equipos", 40000, "Monitor", -2, True)),
        ("Equipo sin nombre", ("S003", "Alquiler de equipos", 40000, "", 2, True)),
        ("Disponibilidad no booleana", ("S005", "Alquiler de equipos", 40000, "Teclado", 2, "sí")),
    ):
        try:
            AlquilerEquipo(*datos)
            fallo(descripcion, AssertionError("El sistema aceptó datos inválidos."))
        except (ValueError, TypeError) as error:
            exitoso(f"{descripcion} detectado: {error}")
        except Exception as error:
            fallo(f"Error inesperado: {descripcion}", error)

    # 3. Servicio no disponible y cambio explícito de booleano.
    try:
        alquiler2 = AlquilerEquipo("S004", "Alquiler de equipos", 60000,
                                   "Proyector Epson", 2, False)
        exitoso("Alquiler no disponible creado correctamente.")
        resultados.append(alquiler2.mostrar_informacion())
    except Exception as error:
        fallo("Error creando alquiler no disponible", error)

    if alquiler2 is not None:
        try:
            if alquiler2.verificar_disponibilidad() is not False:
                raise AssertionError("El equipo debería estar no disponible.")
            exitoso("Se comprobó que el segundo equipo no está disponible.")
            alquiler2.disponible = True
            exitoso(f"Disponibilidad actualizada: {alquiler2.verificar_disponibilidad()}")
        except Exception as error:
            fallo("Error actualizando disponibilidad", error)

    # 4. Reservas de sala: confirmación, procesamiento y validaciones.
    try:
        sala1 = ReservaSala("SAL01", "Reserva de sala", 30000, "Sala principal", 2, True)
        exitoso("Sala disponible creada correctamente.")
    except Exception as error:
        fallo("Error creando sala", error)

    if cliente1 is not None and sala1 is not None:
        try:
            reserva1 = Reserva("R001", cliente1, sala1, 2)
            exitoso("Reserva válida creada correctamente.")
            exitoso(reserva1.confirmar())
            if sala1.verificar_disponibilidad() is not False:
                raise AssertionError("La sala debe quedar ocupada al confirmar.")
            total = reserva1.procesar()
            exitoso(f"Reserva procesada correctamente. Total: ${total:,.2f}")
        except Exception as error:
            fallo("Error procesando reserva válida", error)
    else:
        exitoso("No se creó la reserva válida porque faltó el cliente o la sala.")

    if cliente1 is not None and sala1 is not None:
        for descripcion, duracion in (("Duración negativa", -1), ("Duración booleana", True)):
            try:
                Reserva("R-INV", cliente1, sala1, duracion)
                fallo(descripcion, AssertionError("Se aceptó una reserva inválida."))
            except ValueError as error:
                exitoso(f"{descripcion} rechazada: {error}")
            except Exception as error:
                fallo(f"Error inesperado: {descripcion}", error)

        try:
            sala_ocupada = ReservaSala("SAL02", "Reserva de sala", 20000,
                                       "Sala ocupada", 1, False)
            reserva_ocupada = Reserva("R002", cliente1, sala_ocupada, 1)
            try:
                reserva_ocupada.confirmar()
                fallo("Reserva sin disponibilidad", AssertionError("Se confirmó una sala ocupada."))
            except ReservaInvalidaError as error:
                exitoso(f"Servicio no disponible detectado: {error}")
            except Exception as error:
                fallo("Error inesperado en servicio no disponible", error)
        except Exception as error:
            fallo("Error preparando reserva no disponible", error)

    exitoso("Simulación finalizada.")
    if mostrar:
        for mensaje in resultados:
            print(mensaje)
    return resultados


if __name__ == "__main__":
    ejecutar_simulacion()
