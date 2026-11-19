
# Importación de las clases del proyecto
from cliente import Cliente
from servicio import ReservaSala
from alquiler_equipo import AlquilerEquipo
from asesoria_especializada import AsesoriaEspecializada
from reserva import Reserva

# Importación de la configuración de registros
from configuracion_logs import (
    configurar_logging,
    registrar_evento,
    registrar_error
)


def ejecutar_sistema():

    # Configurar el registro de eventos y errores
    logger = configurar_logging()

    print("=" * 55)
    print("          SISTEMA DE GESTIÓN SOFTWARE FJ")
    print("=" * 55)

    registrar_evento("Inicio del sistema Software FJ")

    # ============================================
    # 1. REGISTRO DE CLIENTE
    # ============================================

    try:
        cliente1 = Cliente(
            "C001",
            "Maria Perez",
            "maria@gmail.com",
            "3001234567"
        )

        print("\n--- CLIENTE REGISTRADO ---")
        print(cliente1.mostrar_informacion())

        registrar_evento("Cliente registrado correctamente")

    except Exception as error:
        print("Error al registrar el cliente:", error)
        registrar_error("Registro de cliente", error)
        return

    # ============================================
    # 2. CREACIÓN DE RESERVA DE SALA
    # ============================================

    try:
        sala = ReservaSala(
            "S001",
            "Sala de reuniones",
            50000,
            "Sala principal",
            2,
            True
        )

        print("\n--- SERVICIO DE SALA ---")
        print(sala.mostrar_informacion())

        registrar_evento("Servicio de sala creado")

    except Exception as error:
        print("Error al crear la sala:", error)
        registrar_error("Creación de sala", error)
        return

    # ============================================
    # 3. CREACIÓN DE RESERVA
    # ============================================

    try:
        reserva1 = Reserva(
            "R001",
            cliente1,
            sala,
            2
        )

        print("\n--- RESERVA CREADA ---")
        print(reserva1.mostrar_informacion())

        registrar_evento("Reserva creada correctamente")

    except Exception as error:
        print("Error al crear la reserva:", error)
        registrar_error("Creación de reserva", error)
        return

    # ============================================
    # 4. CONFIRMACIÓN DE RESERVA
    # ============================================

    try:
        print("\n--- CONFIRMACIÓN DE RESERVA ---")
        print(reserva1.confirmar())

        registrar_evento("Reserva confirmada")

    except Exception as error:
        print("Error al confirmar la reserva:", error)
        registrar_error("Confirmación de reserva", error)

    # ============================================
    # 5. CÁLCULO DEL COSTO
    # ============================================

    try:
        total = reserva1.calcular_total()

        print("\n--- COSTO DE LA RESERVA ---")
        print(f"Total a pagar: ${total:,.0f}")

    except Exception as error:
        print("Error al calcular el costo:", error)
        registrar_error("Cálculo del costo", error)

    # ============================================
    # 6. CREACIÓN DE ALQUILER DE EQUIPO
    # ============================================

    try:
        equipo = AlquilerEquipo(
            "E001",
            "Alquiler de computador",
            30000,
            "Computador portátil",
            3,
            True
        )

        print("\n--- ALQUILER DE EQUIPO ---")
        print(equipo.mostrar_informacion())

        registrar_evento("Alquiler de equipo creado")

    except Exception as error:
        print("Error al crear el alquiler:", error)
        registrar_error("Alquiler de equipo", error)

    # ============================================
    # 7. CREACIÓN DE ASESORÍA ESPECIALIZADA
    # ============================================

    try:
        asesoria = AsesoriaEspecializada(
            "A001",
            "Asesoría informática",
            60000,
            "Sistemas",
            2,
            True
        )

        print("\n--- ASESORÍA ESPECIALIZADA ---")
        print(asesoria.mostrar_informacion())

        registrar_evento("Asesoría creada correctamente")

    except Exception as error:
        print("Error al crear la asesoría:", error)
        registrar_error("Creación de asesoría", error)

    # ============================================
    # 8. PRUEBA DE CLIENTE CON DATOS INCORRECTOS
    # ============================================

    try:
        cliente_invalido = Cliente(
            "C002",
            "",
            "correo_invalido",
            "123"
        )

    except Exception as error:
        print("\n--- PRUEBA DE ERROR ---")
        print("No se pudo registrar el cliente:", error)

        registrar_error("Prueba de cliente inválido", error)

    # ============================================
    # 9. CANCELACIÓN DE RESERVA
    # ============================================

    try:
        print("\n--- CANCELACIÓN DE RESERVA ---")
        print(reserva1.cancelar())

        registrar_evento("Reserva cancelada")

    except Exception as error:
        print("Error al cancelar la reserva:", error)
        registrar_error("Cancelación de reserva", error)

    # ============================================
    # 10. FINALIZACIÓN DEL SISTEMA
    # ============================================

    print("\n" + "=" * 55)
    print("       SISTEMA SOFTWARE FJ FINALIZADO")
    print("=" * 55)

    registrar_evento("Finalización del sistema")


# ============================================
# EJECUCIÓN PRINCIPAL DEL PROGRAMA
# ============================================

if __name__ == "__main__":
    ejecutar_sistema()
