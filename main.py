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
    registrar_error,
)


def ejecutar_sistema():
    # Configurar el registro de eventos y errores
    configurar_logging()

    print("=" * 55)
    print("          SISTEMA DE GESTIÓN SOFTWARE FJ")
    print("=" * 55)

    registrar_evento("Inicio del sistema Software FJ")

    reserva1 = None

    try:
        # ============================================
        # 1. REGISTRO DE CLIENTE
        # ============================================
        try:
            cliente1 = Cliente(
                "C001",
                "Maria Perez",
                "maria@gmail.com",
                "3001234567",
            )
        except Exception as error:
            print("Error al registrar el cliente:", error)
            registrar_error("Registro de cliente", error)
            return
        else:
            print("\n--- CLIENTE REGISTRADO ---")
            print(cliente1.mostrar_informacion())
            registrar_evento("Cliente registrado correctamente")

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
                True,
            )
        except Exception as error:
            print("Error al crear la sala:", error)
            registrar_error("Creación de sala", error)
            return
        else:
            print("\n--- SERVICIO DE SALA ---")
            print(sala.mostrar_informacion())
            registrar_evento("Servicio de sala creado")

        # ============================================
        # 3. CREACIÓN DE RESERVA
        # ============================================
        try:
            reserva1 = Reserva(
                "R001",
                cliente1,
                sala,
                2,
            )
        except Exception as error:
            print("Error al crear la reserva:", error)
            registrar_error("Creación de reserva", error)
            return
        else:
            print("\n--- RESERVA CREADA ---")
            print(reserva1.mostrar_informacion())
            registrar_evento("Reserva creada correctamente")

        # ============================================
        # 4. CONFIRMACIÓN DE RESERVA
        # ============================================
        try:
            mensaje_confirmacion = reserva1.confirmar()
        except Exception as error:
            print("Error al confirmar la reserva:", error)
            registrar_error("Confirmación de reserva", error)
        else:
            print("\n--- CONFIRMACIÓN DE RESERVA ---")
            print(mensaje_confirmacion)
            registrar_evento("Reserva confirmada")

        # ============================================
        # 5. CÁLCULO DEL COSTO
        # ============================================
        try:
            total = reserva1.calcular_total()
        except Exception as error:
            print("Error al calcular el costo:", error)
            registrar_error("Cálculo del costo", error)
        else:
            print("\n--- COSTO DE LA RESERVA ---")
            print(f"Total a pagar: ${total:,.0f}")
            registrar_evento("Costo de reserva calculado: $%s", f"{total:,.0f}")

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
                True,
            )
        except Exception as error:
            print("Error al crear el alquiler:", error)
            registrar_error("Alquiler de equipo", error)
        else:
            print("\n--- ALQUILER DE EQUIPO ---")
            print(equipo.mostrar_informacion())
            registrar_evento("Alquiler de equipo creado")

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
                True,
            )
        except Exception as error:
            print("Error al crear la asesoría:", error)
            registrar_error("Creación de asesoría", error)
        else:
            print("\n--- ASESORÍA ESPECIALIZADA ---")
            print(asesoria.mostrar_informacion())
            registrar_evento("Asesoría creada correctamente")

        # ============================================
        # 8. PRUEBAS DE DATOS Y ESTADOS INVÁLIDOS
        # ============================================
        try:
            Cliente("C002", "", "correo_invalido", "123")
        except Exception as error:
            print("\n--- PRUEBA DE ERROR (CLIENTE INVÁLIDO) ---")
            print("No se pudo registrar el cliente:", error)
            registrar_error("Prueba de cliente inválido", error)

        try:
            reserva_pendiente = Reserva("R002", cliente1, sala, 1)
            reserva_pendiente.procesar()
        except Exception as error:
            print("\n--- PRUEBA DE ERROR (PROCESAR SIN CONFIRMAR) ---")
            print("No se pudo procesar la reserva:", error)
            registrar_error("Prueba de estado de reserva inválido", error)

        # ============================================
        # 9. CANCELACIÓN DE RESERVA
        # ============================================
        if reserva1 is not None:
            try:
                mensaje_cancelacion = reserva1.cancelar()
            except Exception as error:
                print("Error al cancelar la reserva:", error)
                registrar_error("Cancelación de reserva", error)
            else:
                print("\n--- CANCELACIÓN DE RESERVA ---")
                print(mensaje_cancelacion)
                registrar_evento("Reserva cancelada")
        else:
            print("\n--- CANCELACIÓN DE RESERVA ---")
            print("No existe una reserva creada para cancelar.")

    finally:
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
