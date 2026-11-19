"""
Gestiona las reservas de los clientes y los servicios solicitados.
"""

from datetime import datetime
from excepciones import (
    ReservaInvalidaError,
    EstadoReservaError,
    exigir_entero_positivo
)[cite: 6]


class Reserva:
    """Representa una reserva realizada por un cliente."""

    ESTADOS_VALIDOS = ("Pendiente", "Confirmada", "Cancelada", "Procesada")[cite: 6]

    def __init__(self, identificador, cliente, servicio, duracion):
        if not isinstance(identificador, str) or not identificador.strip():
            raise ReservaInvalidaError(
                "El identificador de la reserva no puede estar vacío."
            )[cite: 6]

        if cliente is None or not hasattr(cliente, "mostrar_informacion"):
            raise ReservaInvalidaError(
                "Debe proporcionar un cliente válido."
            )[cite: 6]

        if servicio is None or not callable(
            getattr(servicio, "calcular_costo", None)
        ):
            raise ReservaInvalidaError(
                "Debe proporcionar un servicio válido."
            )[cite: 6]

        exigir_entero_positivo(duracion, "La duración")[cite: 6]

        self.identificador = identificador.strip()[cite: 6]
        self.cliente = cliente[cite: 6]
        self.servicio = servicio[cite: 6]
        self.duracion = duracion[cite: 6]
        self.estado = "Pendiente"[cite: 6]
        self.fecha_creacion = datetime.now()[cite: 6]

    def confirmar(self):
        """Confirma una reserva pendiente."""
        if self.estado != "Pendiente":
            raise EstadoReservaError(
                "Solo se pueden confirmar reservas pendientes."
            )[cite: 6]

        if hasattr(self.servicio, "verificar_disponibilidad") and not self.servicio.verificar_disponibilidad():
            raise ReservaInvalidaError(
                "El servicio no está disponible."
            )[cite: 6]

        if hasattr(self.servicio, "disponible"):
            self.servicio.disponible = False[cite: 6]

        self.estado = "Confirmada"[cite: 6]
        return "La reserva ha sido confirmada correctamente."[cite: 6]

    def cancelar(self):
        """Cancela una reserva pendiente o confirmada."""
        if self.estado not in ("Pendiente", "Confirmada"):
            raise EstadoReservaError(
                "No se puede cancelar una reserva procesada o cancelada."
            )[cite: 6]

        if self.estado == "Confirmada" and hasattr(self.servicio, "disponible"):
            self.servicio.disponible = True[cite: 6]

        self.estado = "Cancelada"[cite: 6]
        return "La reserva ha sido cancelada correctamente."[cite: 6]

    def procesar(self):
        """Procesa una reserva que ya fue confirmada."""
        if self.estado != "Confirmada":
            raise EstadoReservaError(
                "Solo se pueden procesar reservas confirmadas."
            )[cite: 6]

        costo = self.calcular_total()[cite: 6]

        if isinstance(costo, bool) or not isinstance(costo, (int, float)) or costo < 0:
            raise ReservaInvalidaError(
                "El servicio generó un costo inválido."
            )[cite: 6]

        self.estado = "Procesada"[cite: 6]
        return costo[cite: 6]

    def calcular_total(self):
        """Obtiene el costo total calculado por el servicio."""
        costo_base = self.servicio.calcular_costo()[cite: 6]

        if isinstance(costo_base, bool) or not isinstance(costo_base, (int, float)) or costo_base < 0:
            raise ReservaInvalidaError(
                "No fue posible calcular el costo del servicio."
            )[cite: 6]

        return costo_base[cite: 6]

    def mostrar_informacion(self):
        """Muestra los datos principales de la reserva."""
        info_servicio = (
            self.servicio.mostrar_informacion()
            if hasattr(self.servicio, "mostrar_informacion")
            else str(self.servicio)
        )[cite: 6]

        return (
            f"\n--- INFORMACIÓN DE LA RESERVA ---\n"
            f"Identificador: {self.identificador}\n"
            f"Cliente: {self.cliente.mostrar_informacion()}\n"
            f"Servicio: {info_servicio}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}\n"
            f"Fecha de creación: {self.fecha_creacion.strftime('%d/%m/%Y %H:%M')}\n"
            f"Costo total: ${self.calcular_total():,.2f}\n"
        )[cite: 6]
