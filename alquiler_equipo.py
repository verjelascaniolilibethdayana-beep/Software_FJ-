"""
Proyecto: Software FJ
Archivo: alquiler_equipo.py

Descripción:
Clase que representa el servicio de alquiler de equipos.
"""

from servicio import Servicio


class AlquilerEquipo(Servicio):
    """Representa el servicio de alquiler de equipos."""

    def __init__(
        self,
        identificador,
        nombre_servicio,
        precio_base,
        nombre_equipo,
        dias_alquiler,
        disponible=True
    ):
        # Inicializa los atributos heredados de la clase Servicio.
        super().__init__(identificador, nombre_servicio, precio_base)

        # Inicializa los atributos propios del alquiler de equipos.
        self.nombre_equipo = nombre_equipo
        self.dias_alquiler = dias_alquiler
        self.disponible = disponible

    @property
    def nombre_equipo(self):
        return self._nombre_equipo

    @nombre_equipo.setter
    def nombre_equipo(self, valor):
        # Valida que el nombre del equipo no esté vacío.
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del equipo no puede estar vacío.")

        self._nombre_equipo = valor.strip()

    @property
    def dias_alquiler(self):
        return self._dias_alquiler

    @dias_alquiler.setter
    def dias_alquiler(self, valor):
        # Valida que el valor sea un entero positivo y no un booleano.
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise TypeError("Los días de alquiler deben ser un número entero.")

        if valor <= 0:
            raise ValueError("Los días de alquiler deben ser mayores que cero.")

        self._dias_alquiler = valor

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        # Valida que la disponibilidad sea booleana.
        if not isinstance(valor, bool):
            raise TypeError("La disponibilidad debe ser True o False.")

        self._disponible = valor

    def calcular_costo(self):
        # Calcula el costo total multiplicando el precio base por los días.
        return self.precio_base * self.dias_alquiler

    def verificar_disponibilidad(self):
        # Retorna si el equipo está disponible o no.
        return self.disponible

    def mostrar_informacion(self):
        # Construye y devuelve un resumen del alquiler.
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"ID: {self.identificador} | "
            f"Servicio: {self.nombre_servicio} | "
            f"Equipo: {self.nombre_equipo} | "
            f"Días: {self.dias_alquiler} | "
            f"Precio por día: ${self.precio_base:,.2f} | "
            f"Costo total: ${self.calcular_costo():,.2f} | "
            f"Estado: {estado}"
        )