Contiene la clase abstracta Servicio y la clase ReservaSala.
"""

from abc import ABC, abstractmethod


class Servicio(ABC):
    """Clase abstracta que representa un servicio general."""

    def __init__(self, identificador, nombre_servicio, precio_base):
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador no puede estar vacío.")

        if not isinstance(nombre_servicio, str) or not nombre_servicio.strip():
            raise ValueError("El nombre del servicio no puede estar vacío.")

        if isinstance(precio_base, bool) or not isinstance(precio_base, (int, float)):
            raise TypeError("El precio debe ser numérico.")

        if precio_base <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self.identificador = identificador.strip()
        self.nombre_servicio = nombre_servicio.strip()
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self):
        """Calcula el costo total del servicio."""
        pass

    @abstractmethod
    def verificar_disponibilidad(self):
        """Comprueba si el servicio está disponible."""
        pass

    @abstractmethod
    def mostrar_informacion(self):
        """Muestra la información del servicio."""
        pass


class ReservaSala(Servicio):
    """Servicio especializado para reservar salas."""

    def __init__(
        self,
        identificador,
        nombre_servicio,
        precio_base,
        nombre_sala,
        horas,
        disponible=True
    ):
        super().__init__(identificador, nombre_servicio, precio_base)

        if not isinstance(nombre_sala, str) or not nombre_sala.strip():
            raise ValueError("El nombre de la sala no puede estar vacío.")

        if isinstance(horas, bool) or not isinstance(horas, int) or horas <= 0:
            raise ValueError("Las horas deben ser un entero positivo.")

        if not isinstance(disponible, bool):
            raise TypeError("La disponibilidad debe ser verdadera o falsa.")

        self.nombre_sala = nombre_sala.strip()
        self.horas = horas
        self.disponible = disponible

    def calcular_costo(self):
        """Calcula el costo según las horas de reserva."""
        return self.precio_base * self.horas

    def verificar_disponibilidad(self):
        """Indica si la sala está disponible."""
        return self.disponible

    def mostrar_informacion(self):
        """Devuelve los datos de la reserva de sala."""
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"ID: {self.identificador} | "
            f"Servicio: {self.nombre_servicio} | "
            f"Sala: {self.nombre_sala} | "
            f"Horas: {self.horas} | "
            f"Precio por hora: ${self.precio_base:,.2f} | "
            f"Costo total: ${self.calcular_costo():,.2f} | "
            f"Estado: {estado}"
