"""
Proyecto: Software FJ
Archivo: asesoria_especializada.py

Descripción:
Clase que representa el servicio de asesoría especializada.
"""

from servicio import Servicio


class AsesoriaEspecializada(Servicio):
    """Representa un servicio de asesoría especializada."""

    def __init__(
        self,
        identificador,
        nombre_servicio,
        precio_base,
        area_especialidad,
        horas,
        disponible=True
    ):
        # Inicializa los atributos heredados de la clase Servicio.
        super().__init__(identificador, nombre_servicio, precio_base)

        # Inicializa los atributos propios del servicio.
        self.area_especialidad = area_especialidad
        self.horas = horas
        self.disponible = disponible

    @property
    def area_especialidad(self):
        return self._area_especialidad

    @area_especialidad.setter
    def area_especialidad(self, valor):
        # Valida que el área sea un texto no vacío.
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El área de especialidad no puede estar vacía.")

        self._area_especialidad = valor.strip()

    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self, valor):
        # Valida que las horas sean un número entero y no un booleano.
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise TypeError("Las horas deben ser un número entero.")

        if valor <= 0:
            raise ValueError("Las horas deben ser mayores que cero.")

        self._horas = valor

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
        # Calcula el costo total multiplicando la tarifa base por las horas.
        return self.precio_base * self.horas

    def verificar_disponibilidad(self):
        # Retorna si la asesoría está disponible o no.
        return self.disponible

    def mostrar_informacion(self):
        # Construye y devuelve un resumen del servicio.
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"ID: {self.identificador} | "
            f"Servicio: {self.nombre_servicio} | "
            f"Área: {self.area_especialidad} | "
            f"Horas: {self.horas} | "
            f"Precio por hora: ${self.precio_base:,.2f} | "
            f"Costo total: ${self.calcular_costo():,.2f} | "
            f"Estado: {estado}"
        )
