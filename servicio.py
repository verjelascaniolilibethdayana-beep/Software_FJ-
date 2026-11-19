"""
Contiene la clase abstracta Servicio y la clase ReservaSala.
"""

from abc import ABC, abstractmethod


class Servicio(ABC):
    """Clase abstracta que representa un servicio general."""

    def __init__(self, identificador, nombre_servicio, precio_base):
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador no puede estar vacío.")[cite: 3]

        if not isinstance(nombre_servicio, str) or not nombre_servicio.strip():
            raise ValueError("El nombre del servicio no puede estar vacío.")[cite: 3]

        if isinstance(precio_base, bool) or not isinstance(precio_base, (int, float)):
            raise TypeError("El precio debe ser numérico.")[cite: 3]

        if precio_base <= 0:
            raise ValueError("El precio debe ser mayor que cero.")[cite: 3]

        self.identificador = identificador.strip()[cite: 3]
        self.nombre_servicio = nombre_servicio.strip()[cite: 3]
        self.precio_base = precio_base[cite: 3]

    @abstractmethod
    def calcular_costo(self):
        """Calcula el costo total del servicio."""
        pass[cite: 3]

    @abstractmethod
    def verificar_disponibilidad(self):
        """Comprueba si el servicio está disponible."""
        pass[cite: 3]

    @abstractmethod
    def mostrar_informacion(self):
        """Muestra la información del servicio."""
        pass[cite: 3]


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
        super().__init__(identificador, nombre_servicio, precio_base)[cite: 3]

        if not isinstance(nombre_sala, str) or not nombre_sala.strip():
            raise ValueError("El nombre de la sala no puede estar vacío.")[cite: 3]

        if isinstance(horas, bool) or not isinstance(horas, int) or horas <= 0:
            raise ValueError("Las horas deben ser un entero positivo.")[cite: 3]

        if not isinstance(disponible, bool):
            raise TypeError("La disponibilidad debe ser verdadera o falsa.")[cite: 3]

        self.nombre_sala = nombre_sala.strip()[cite: 3]
        self.horas = horas[cite: 3]
        self.disponible = disponible[cite: 3]

    def calcular_costo(self):
        """Calcula el costo según las horas de reserva."""
        return self.precio_base * self.horas[cite: 3]

    def verificar_disponibilidad(self):
        """Indica si la sala está disponible."""
        return self.disponible[cite: 3]

    def mostrar_informacion(self):
        """Devuelve los datos de la reserva de sala."""
        estado = "Disponible" if self.disponible else "No disponible"[cite: 3]

        return (
            f"ID: {self.identificador} | "
            f"Servicio: {self.nombre_servicio} | "
            f"Sala: {self.nombre_sala} | "
            f"Horas: {self.horas} | "
            f"Precio por hora: ${self.precio_base:,.2f} | "
            f"Costo total: ${self.calcular_costo():,.2f} | "
            f"Estado: {estado}"
        )[cite: 3]
